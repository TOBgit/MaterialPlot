# -*- coding:utf-8 -*-
import PySide2.QtGui
from PySide2.QtWidgets import QListView, QStyledItemDelegate, QCheckBox, QLineEdit, QLabel, QHBoxLayout, QFrame, QMenu, QAction
from PySide2.QtCore import QPointF, QRectF, Qt, Signal, QModelIndex
from PySide2.QtGui import QTransform, QStandardItemModel, QStandardItem
from .AxisObjects import MarkLine, VerticalMarkLine, VShadowMarkLine, HShadowMarkLine, IndicatorLines
import math

class ListItemModel(QStandardItemModel):
    pass

class ListItem(QStandardItem):
    ROLE_A1 = Qt.UserRole + 1
    ROLE_A2 = Qt.UserRole + 2
    ROLE_B1 = Qt.UserRole + 3
    ROLE_B2 = Qt.UserRole + 4
    ROLE_C = Qt.UserRole + 5
    ROLE_V = Qt.UserRole +6
    def __init__(self, a1, a2, b1, b2, c, visible):
        super(ListItem, self).__init__()
        self.visible = visible
        self.setData(a1, self.ROLE_A1)
        self.setData(a2, self.ROLE_A2)
        self.setData(b1, self.ROLE_B1)
        self.setData(b2, self.ROLE_B2)
        self.setData(c, self.ROLE_C)
        self.setData(visible, self.ROLE_V)

    def exportData(self):
        return {
            "a1": self.data(self.ROLE_A1),
            "b1": self.data(self.ROLE_B1),
            "b2": self.data(self.ROLE_B2),
            "a2": self.data(self.ROLE_A2),
            "c": self.data(self.ROLE_C),
            "visible": self.data(self.ROLE_V)
        }

    def data(self, role):
        if role == Qt.DisplayRole:
            return ""
        return super(ListItem, self).data(role)


class ItemWidget(QFrame):
    EditFinished = Signal(QModelIndex, dict)
    def __init__(self, parent, index):
        super(ItemWidget, self).__init__(parent)
        self.index = index
        self.checkbox = QCheckBox()
        self.a1line = QLineEdit()
        self.a2line = QLineEdit()
        self.b1line = QLineEdit()
        self.b2line = QLineEdit()
        self.cline = QLineEdit()

        hlayout = QHBoxLayout()
        self.setLayout(hlayout)

        hlayout.addWidget(self.checkbox)
        hlayout.addWidget(self.a1line)
        hlayout.addWidget(QLabel("* X ^"))
        hlayout.addWidget(self.a2line)
        hlayout.addWidget(QLabel("/"))
        hlayout.addWidget(self.b1line)
        hlayout.addWidget(QLabel("* Y ^"))
        hlayout.addWidget(self.b2line)
        hlayout.addWidget(QLabel("="))
        hlayout.addWidget(self.cline)

        self.a1line.editingFinished.connect(self.onFinishEdit)
        self.a2line.editingFinished.connect(self.onFinishEdit)
        self.b1line.editingFinished.connect(self.onFinishEdit)
        self.b2line.editingFinished.connect(self.onFinishEdit)
        self.cline.editingFinished.connect(self.onFinishEdit)
        self.checkbox.stateChanged.connect(self.onFinishEdit)

        hlayout.setContentsMargins(0,0,0,0)

    def getData(self):
        return  {
            "a1": float(self.a1line.text()),
            "b1": float(self.b1line.text()),
            "b2": float(self.b2line.text()),
            "a2": float(self.a2line.text()),
            "c": float(self.cline.text()),
            "visible": self.checkbox.isChecked()
        }

    def onFinishEdit(self, *args):
        self.EditFinished.emit(self.index, self.getData())

    def setData(self, a1, a2, b1, b2, c, visible):
        self.a1line.setText(str(a1))
        self.a2line.setText(str(a2))
        self.b1line.setText(str(b1))
        self.b2line.setText(str(b2))
        self.cline.setText(str(c))
        self.checkbox.setChecked(visible)



class ADelegate(QStyledItemDelegate):
    def __init__(self, parent):
        super(ADelegate, self).__init__(parent)

    def setEditorData(self, editor, index):
        editor.setData(
            index.data(ListItem.ROLE_A1),
            index.data(ListItem.ROLE_A2),
            index.data(ListItem.ROLE_B1),
            index.data(ListItem.ROLE_B2),
            index.data(ListItem.ROLE_C),
            index.data(ListItem.ROLE_V),
        )

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def createEditor(self, parent, option, index):
        editor = ItemWidget(parent, index)
        editor.setData(
            index.data(ListItem.ROLE_A1),
            index.data(ListItem.ROLE_A2),
            index.data(ListItem.ROLE_B1),
            index.data(ListItem.ROLE_B2),
            index.data(ListItem.ROLE_C),
            index.data(ListItem.ROLE_V),
        )
        editor.EditFinished.connect(self.parent().onEditFinished)
        return editor


class AListView(QListView):
    EditFinished = Signal()
    def __init__(self, parent):
        super(AListView, self).__init__(parent)
        self.delegate = ADelegate(self)
        self.model = ListItemModel()

        self.setModel(self.model)
        self.setItemDelegate(self.delegate)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.onCustomMenu)


    def onCustomMenu(self, pos):
        indexes = self.selectedIndexes()

        menu = QMenu(self)
        # load model action
        deleteAction = QAction("Delete Line")
        addAction = QAction("Add Line")
        menu.addAction(addAction)
        menu.addAction(deleteAction)
        if indexes:
            addAction.setVisible(False)
        else:
            deleteAction.setVisible(False)


        deleteAction.triggered.connect(self._deleteItem)
        addAction.triggered.connect(self.addItem)
        globalPoint = self.mapToGlobal(pos)
        menu.exec_(globalPoint)

    def onEditFinished(self, index, data):
        self.model.setData(index, data["a1"], ListItem.ROLE_A1)
        self.model.setData(index, data["a2"], ListItem.ROLE_A2)
        self.model.setData(index, data["b1"], ListItem.ROLE_B1)
        self.model.setData(index, data["b2"], ListItem.ROLE_B2)
        self.model.setData(index, data["c"], ListItem.ROLE_C)
        self.model.setData(index, data["visible"], ListItem.ROLE_V)
        self.EditFinished.emit()

    def addItem(self):
        item = ListItem(1.0,1.0,1.0,1.0,1.0,False)
        self.model.appendRow(item)
        self.openPersistentEditor(item.index())
        self.EditFinished.emit()

    def _deleteItem(self):
        for index in self.selectedIndexes():
            self.model.removeRow(index.row())

    def popSelectedItem(self):
        if self.model.rowCount() == 0:
            return
        self._deleteItem()
        self.EditFinished.emit()

    def getData(self):
        data = []
        for row in range(self.model.rowCount()):
            data.append(self.model.item(row).exportData())
        return data