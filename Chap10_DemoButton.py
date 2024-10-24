#Chap10_DemoButton.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DemoForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        btn1 = QPushButton("닫기", self)
        btn1.move(20, 20)
        btn1.clicked.connect(QCoreApplication.instance().quit)

#진입점체크 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_() 
