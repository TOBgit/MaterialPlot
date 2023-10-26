import pandas as pd
from PySide2.QtCore import QAbstractTableModel, QModelIndex, Qt


class TableModel(QAbstractTableModel):
    def __init__(self, model):
        super(TableModel, self).__init__()
        self.model = model
        self.hHeader = self.model.raw_data.columns.tolist()
        # self.vHeader = self.data.index.tolist()
        
    def rowCount(self, parent=QModelIndex()):
        return self.model.raw_data.shape[0]
    
    def columnCount(self, parent=QModelIndex()):
        return self.model.raw_data.shape[1]
    
    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        if role == Qt.DisplayRole:
            return str(self.model.raw_data.iloc[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.hHeader[section]
        elif orientation == Qt.Vertical:
            return section
        
    def setData(self, index, value, role=Qt.EditRole):
        row = index.row()
        if index.isValid() and (0 <= row < self.rowCount()) and value:
            col = index.column()
            if 0 <= col < self.columnCount():
                self.beginResetModel()
                try:
                    dtype = type(self.model.raw_data.iloc[row, col])
                    self.model.raw_data.iloc[row, col] = dtype(value)
                except Exception:
                    dtype = type(self.model.raw_data.iloc[row-1, col])
                    self.model.raw_data.iloc[row, col] = dtype(value)
                self.model.onRawDataUpdate()
                self.dirty = True
                self.endResetModel()
                return True
        return False
    
    
    def insertRows(self, position=-1, rows=1, index=QModelIndex()):
        position = self.rowCount()
        if position > 0:
            self.beginInsertRows(QModelIndex(), position, position+rows-1)
            self.model.raw_data = pd.concat([self.model.raw_data, pd.DataFrame([[pd.NA]*self.columnCount()], columns=self.model.raw_data.columns)])
            self.endInsertRows()
            self.dirty = True
            return True
        return False
    
    def deleteRows(self):
        pass

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index)|Qt.ItemIsEditable|Qt.ItemIsSelectable)