# -*- coding:utf-8 -*-
from PySide2.QtWidgets import QTreeView, QStyledItemDelegate, QLabel, QHBoxLayout, QFrame, QMenu, QAction, QColorDialog, \
    QDialog, QToolButton
from PySide2.QtGui import QColor, QIcon
from PySide2.QtCore import Qt
from .TreeModel import TreeItemModel
from PySide2.QtCore import Signal
import PySide2

class EyeLabel(QToolButton):
    def __init__(self, parent, index):
        super(EyeLabel, self).__init__(parent)
        # self.setMaximumWidth(20)
        # self.setMinimumHeight(20)
        self.index = index
        self.setStyleSheet("QToolButton{border:None;}")
        self.setFixedSize(20, 20)
        self.setCheckable(True)
        self.setChecked(True)

        # self.setPixmap(pix)
        # self.setScaledContents(True)
        self.clicked.connect(self.OnToggled)
    def setChecked(self, checked):
        super(EyeLabel, self).setChecked(checked)

        self.updateState()
    def updateState(self):
        checked = self.isChecked()
        if checked:
            self.setIcon(QIcon(u"./Res/Visible.svg"))
        else:
            self.setIcon(QIcon(u"./Res/Unvisible.svg"))

    def OnToggled(self, *args):

        self.index.model().setData(self.index, Qt.Checked if self.isChecked() else Qt.Unchecked, Qt.UserRole)
        self.updateState()

class ColorLabel(QLabel):
    def __init__(self, parent, index):
        super(ColorLabel, self).__init__(parent)
        self.setMaximumWidth(100)
        self.setMinimumHeight(20)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(lambda x: self.onContext(index, x))

    def setColor(self, color):
        if isinstance(color, list):
            self.setStyleSheet("QFrame{background-color:rgb(%d, %d, %d);}" % (color[0], color[1], color[2]))

    def onContext(self, index, pos):
        print(index, pos)

        menu = QMenu(self)
        selectAction = QAction("Select Color...")
        pickAction = QAction("Pick Color")

        pickAction.setEnabled(False)  # todo: not implemented

        menu.addAction(selectAction)
        menu.addAction(pickAction)

        selectAction.triggered.connect(lambda: self.onSelect(index))
        pickAction.triggered.connect(lambda: self.onPick(index))
        globalPoint = self.mapToGlobal(pos)
        menu.exec_(globalPoint)

    def onSelect(self, index):
        dlg = QColorDialog()
        dlg.setOption(QColorDialog.ShowAlphaChannel)
        color = index.data(Qt.BackgroundColorRole)
        dlg.setCurrentColor(QColor(*color))
        if dlg.exec_() == QDialog.Accepted:
            c = dlg.currentColor()
            color = [c.red(), c.green(), c.blue()]
            index.model().setData(index, color, Qt.BackgroundColorRole)
            self.setColor(color)

    def onPick(self, index):
        pass


class MyDelegate(QStyledItemDelegate):
    def createEditor(self, parent: PySide2.QtWidgets.QWidget, option: PySide2.QtWidgets.QStyleOptionViewItem,
                     index: PySide2.QtCore.QModelIndex):
        layout = QHBoxLayout()
        frame = QFrame(parent)
        frame.setLayout(layout)
        frame.setContentsMargins(0, 0, 0, 0)
        layout.setContentsMargins(2, 2, 2, 2)

        label = QFrame(frame)
        layout.addWidget(label)
        eyelabel = EyeLabel(frame, index)
        layout.addWidget(eyelabel)
        frame.eyelabel = eyelabel
        color = index.data(Qt.BackgroundColorRole)
        if color is not None:
            colorlabel = ColorLabel(frame, index)
            colorlabel.setColor(color)
            layout.addWidget(colorlabel)
        return frame

    def setEditorData(self, editor:PySide2.QtWidgets.QWidget, index:PySide2.QtCore.QModelIndex) -> None:
        editor.eyelabel.setChecked(index.data(Qt.UserRole) == Qt.Checked)
        super(MyDelegate, self).setEditorData(editor, index)


class TreeView(QTreeView):
    OnSelectionChanged = Signal(dict)

    def __init__(self, parent):
        super(TreeView, self).__init__(parent)
        self.model = TreeItemModel()
        self.setModel(self.model)
        self.setSelectionMode(QTreeView.ExtendedSelection)
        self.model.MyDataChanged.connect(self.onDataChanged)
        self.setItemDelegate(MyDelegate())

    def onDataChanged(self):
        self.OnSelectionChanged.emit(self.model.getAllCheckedItems())

    def getSelections(self):
        return self.model.getAllCheckedItems()

    def clearModel(self):
        self.model.clear()

    def addFamilies(self, families):
        for family in families:
            family = self.model.addFamily(family)
            self.openPersistentEditor(family.index())

    def addItem(self, item, family=None):
        item = self.model.addItemByFamily(item.label, [item.color_r, item.color_g, item.color_b], family)
        self.openPersistentEditor(item.index())
