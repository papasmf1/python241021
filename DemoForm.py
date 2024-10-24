# DemoForm.py 
# DemoForm.ui(화면단) + DemoForm.py(로직단) 
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#미리 디자인한 문서를 로딩 
form_class = uic.loadUiType("DemoForm.ui")[0]

#DemoForm클래스 정의 
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 윈도우")

#진입점 체크 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm()
    myWindow.show()
    app.exec_()
    
