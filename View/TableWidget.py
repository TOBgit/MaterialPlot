from PySide2.QtCore import Qt, QAbstractTableModel, QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTableView, QPushButton
from View.TableModel import TableModel

class ManageItem(QWidget):
    def __init__(self, model):
        super(ManageItem, self).__init__()
        
        layout0 = QVBoxLayout()
        layout1 = QHBoxLayout()
        self.addButton = QPushButton("Add Item")
        self.deleteButton = QPushButton("Delete Item")
        layout1.addWidget(self.addButton)
        layout1.addWidget(self.deleteButton)

        self.tableModel = TableModel(model)
        self.table = QTableView()
        self.table.setModel(self.tableModel)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        layout2 = QHBoxLayout()
        layout2.addWidget(self.table)
        layout0.addLayout(layout1)
        layout0.addLayout(layout2)

        self.setLayout(layout0)
        self.resize(1200, 800)

        self.addButton.clicked.connect(self.tableModel.insertRows)

class ManageSelection(QWidget):
    def __init__(self):
        super(ManageItem, self).__init__()

        layout0 = QVBoxLayout()
        layout1 = QHBoxLayout()
        self.addButton = QPushButton("Add Selection")
        self.deleteButton = QPushButton("Delete Selection")
        layout1.addWidget(self.addButton)
        layout1.addWidget(self.deleteButton)

        #TODO(HH) shall we create a new pd dataframe to store the points for lines?
        pass