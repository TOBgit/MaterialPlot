# -*- coding:utf-8 -*-
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt, Signal


class TreeItem(QStandardItem):
    def __init__(self, name):
        super(TreeItem, self).__init__(name)
        self.setCheckable(True)
        self.setTristate(True)
        self.setCheckState(Qt.Checked)
        self.name = name

    def data(self, role: int):
        if role == Qt.DisplayRole:
            return self.name
        return super(TreeItem, self).data(role)

    def setData(self, value, role):
        if role == Qt.CheckStateRole:
            if value == int(Qt.Checked):
                for i in range(self.rowCount()):
                    child = self.child(i)
                    child.setData(Qt.Checked, role)
                super(TreeItem, self).setData(value, role)
                if self.parent():
                    self.parent().setData(1, role)
            elif value == int(Qt.PartiallyChecked):
                childrencount = self.rowCount()
                if childrencount > 0:
                    checkedcount = 0
                    for i in range(self.rowCount()):
                        child = self.child(i)
                        if child.checkState() == Qt.Checked:
                            checkedcount += 1
                    if checkedcount == childrencount:
                        value = 2
                    elif checkedcount == 0:
                        value = 0
                else:
                    value = 1
            else:
                for i in range(self.rowCount()):
                    child = self.child(i)
                    child.setData(0, role)
                super(TreeItem, self).setData(value, role)
                if self.parent():
                    self.parent().setData(1, role)

        return super(TreeItem, self).setData(value, role)


class TreeItemModel(QStandardItemModel):
    MyDataChanged = Signal()
    def __init__(self):
        super(TreeItemModel, self).__init__()
        self.rootitem = self.invisibleRootItem()

    def getAllCheckedItems(self):
        data = {"Families": [], "Items": []}
        for row in range(self.rowCount()):
            family = self.item(row)
            if family.checkState() == Qt.Checked:
                data["Families"].append(family.name)
            for row2 in range(family.rowCount()):
                item = family.child(row2)
                if item.checkState() == Qt.Checked:
                    data["Items"].append(item.name)
        return data

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
    #
    def setData(self, index, value, role):
        ret = super(TreeItemModel, self).setData(index, value, role)
        self.MyDataChanged.emit()
        return ret
    #     if not index.isValid():
    #         return False
    #     if role == Qt.CheckStateRole:
    #         item = self.itemFromIndex(index)
    #
    #         if value == int(Qt.Checked):
    #             item.setCheckState(Qt.Checked)
    #             for i in range(item.rowCount()):
    #                 child = item.child(i)
    #                 child.setData(Qt.Checked, role)
    #             if item.parent():
    #                 item.parent().setData(Qt.PartiallyChecked, role)
    #         elif value == int(Qt.PartiallyChecked):
    #             childrencount = len(self.children())
    #             if childrencount > 0:
    #                 checkedcount = 0
    #                 for i in range(item.rowCount()):
    #                     child = item.child(i)
    #                     if child.checkState() == Qt.Checked:
    #                         checkedcount += 1
    #                 if checkedcount == childrencount:
    #                     item.setCheckState(Qt.Checked)
    #                 elif checkedcount == 0:
    #                     item.setCheckState(Qt.UnChecked)
    #                 else:
    #                     item.setCheckState(Qt.PartiallyChecked)
    #             else:
    #                 item.setCheckState(Qt.PartiallyChecked)
    #         else:
    #             for i in range(item.rowCount()):
    #                 child = item.child(i)
    #                 child.setData(Qt.Unchecked, role)
    #             if item.parent():
    #                 item.parent().setData(Qt.PartiallyChecked, role)
    #             item.setCheckState(Qt.Unchecked)
    #
    #         # item.setCheckState(Qt.CheckState.Checked if value == int(Qt.Checked) else Qt.CheckState.Unchecked)
    #         self.dataChanged.emit(index, index)
    #         return True
    #     return super(TreeItemModel, self).setData(index, value, role)


    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.CheckStateRole:
            item = self.itemFromIndex(index)
            return item.checkState()
        return super(TreeItemModel, self).data(index, role)

    def addFamily(self, familyname):
        familyItem = TreeItem(familyname)
        self.appendRow(familyItem)
        return familyItem

    def addItemByFamily(self, label, family=None):
        if not family:
            item = TreeItem(label)
            self.appendRow(item)
            return item
        items = self.findItems(family, Qt.MatchRecursive)
        if not items:
            familyitem = self.addFamily(family)
        else:
            familyitem = items[0]
        item = TreeItem(label)
        familyitem.appendRow(item)
        return item
