# -*- coding:utf-8 -*-
from PySide2.QtWidgets import QTreeView
from .TreeModel import TreeItemModel
from PySide2.QtCore import Signal


class TreeView(QTreeView):
    OnSelectionChanged = Signal(dict)

    def __init__(self, parent):
        super(TreeView, self).__init__(parent)
        self.model = TreeItemModel()
        self.setModel(self.model)
        self.setSelectionMode(QTreeView.ExtendedSelection)
        self.model.MyDataChanged.connect(self.onDataChanged)

    def onDataChanged(self):
        self.OnSelectionChanged.emit(self.model.getAllCheckedItems())

    def getSelections(self):
        return self.model.getAllCheckedItems()

    def clearModel(self):
        self.model.clear()

    def addFamilies(self, families):
        for family in families:
            self.model.addFamily(family)

    def addItem(self, item, family=None):
        self.model.addItemByFamily(item.label, family)
