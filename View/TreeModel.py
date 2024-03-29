# -*- coding:utf-8 -*-
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt, Signal


class TreeItem(QStandardItem):
    def __init__(self, name, color=None):
        super(TreeItem, self).__init__(name)
        # self.setCheckable(True)
        # self.setTristate(True)
        # self.setCheckState(Qt.Checked)
        self.name = name
        self.color = color

    def data(self, role: int):
        if role == Qt.DisplayRole:
            return self.name
        elif role == Qt.BackgroundColorRole:
            return self.color
        return super(TreeItem, self).data(role)

    def setData(self, value, role):
        if role == Qt.UserRole:
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
        data = {"Families": [], "Items": {}}
        for row in range(self.rowCount()):
            family = self.item(row)
            if family.checkState() == Qt.Checked:
                data["Families"].append(family.name)
            for row2 in range(family.rowCount()):
                item = family.child(row2)
                if item.data(Qt.UserRole) == Qt.Checked:
                    data["Items"][item.name] = {"color":item.color}
        return data

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled

    #
    def setData(self, index, value, role):
        ret = super(TreeItemModel, self).setData(index, value, role)
        self.MyDataChanged.emit()
        return ret

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        # if role == Qt.CheckStateRole:
        #     item = self.itemFromIndex(index)
        #     return item.checkState()
        return super(TreeItemModel, self).data(index, role)

    def addFamily(self, familyname):
        familyItem = TreeItem(familyname)
        self.appendRow(familyItem)
        return familyItem

    def addItemByFamily(self, label, color, family=None):
        if not family:
            item = TreeItem(label, color)
            self.appendRow(item)
            return item
        items = self.findItems(family, Qt.MatchRecursive)
        if not items:
            familyitem = self.addFamily(family)
        else:
            familyitem = items[0]
        item = TreeItem(label, color)
        familyitem.appendRow(item)
        return item
