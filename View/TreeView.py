# -*- coding:utf-8 -*-
from PySide2.QtWidgets import QTreeView, QStyledItemDelegate, QLabel, QHBoxLayout, QFrame, QMenu, QAction, QColorDialog, \
    QDialog
from PySide2.QtGui import QPalette, QColor
from PySide2.QtCore import Qt
from .TreeModel import TreeItemModel
from PySide2.QtCore import Signal
import PySide2


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

        color = index.data(Qt.BackgroundColorRole)
        colorlabel = ColorLabel(frame, index)
        colorlabel.setColor(color)
        layout.addWidget(label)
        layout.addWidget(colorlabel)
        return frame


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
            # self.openPersistentEditor(family.index())

    def addItem(self, item, family=None):
        item = self.model.addItemByFamily(item.label, [item.color_r, item.color_g, item.color_b], family)
        self.openPersistentEditor(item.index())
