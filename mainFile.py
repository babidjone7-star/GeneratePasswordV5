import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QLabel, QDialog
from Pysidep import Ui_Dialog
import string
import random

Password ="" #пароль - для записи с символами
RealPassword = "" #используется для убирания символов
arr = list(string.ascii_letters + string.ascii_uppercase + string.ascii_lowercase + string.digits)

class Gener(QDialog):
    def __init__(self, /):
        self.CurPass = ""
        self.HowMuchCopy = 0
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.generateButton.clicked.connect(self.onClick)   
        self.ui.CopyBut.clicked.connect(self.Copy) 
    def onClick(self):
        global Password
        global RealPassword
        global CurPassword
        Password = random.choices(arr, k=8)
        RealPassword = "".join(Password)
        self.ui.ParoleLabel.setText(f"Твой пароль: {RealPassword}")
        self.CurPass = RealPassword
    def Copy(self):
        self.HowMuchCopy = self.HowMuchCopy + 1
        self.ui.CopyBut.setText(f"Скопировано, ты скопировал раз {self.HowMuchCopy}")
        QApplication.clipboard().setText(self.CurPass)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wing = Gener()
    wing.show()
    sys.exit(app.exec())