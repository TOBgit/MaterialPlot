from PySide2.QtWidgets import QVBoxLayout, QLabel, QDialog, QDialogButtonBox

class simpleErrorPopUp(QDialog):
    def __init__(self, error_message: str):
        super().__init__()
        self.setWindowTitle("ERROR")
        # self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel(error_message))
        # self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


