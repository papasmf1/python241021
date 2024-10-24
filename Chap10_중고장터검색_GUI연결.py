#Chap09_중고장터검색_GUI연결.py
import sys
from PyQt5.QtWidgets import *
import urllib.request
from bs4 import BeautifulSoup
import webbrowser   #브라우저로 넘기는 경우 
import re 

class DemoForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        #창의 시작위치와 폭, 높이(x,y,width,height) 
        self.setGeometry(200, 200, 800, 600)
        
        #입력 텍스트 
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(20, 20)
        #기본 문자열 출력 
        self.lineEdit.setText("아이폰")

        #버튼
        self.btn = QPushButton("검색", self)
        self.btn.move(120, 20)
        self.btn.clicked.connect(self.setTableWidgetData)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(20, 70)
        self.tableWidget.resize(700, 500)
        self.tableWidget.setRowCount(100)  #행의 갯수 
        self.tableWidget.setColumnCount(2)  #컬럼의 갯수 
        #컬럼의 폭을 지정한다. 0번 1번 
        self.tableWidget.setColumnWidth(0, 400)
        self.tableWidget.setColumnWidth(1, 200)

        #QTableWidget의 헤더 셋팅하기
        self.tableWidget.setHorizontalHeaderLabels(["중고장터 매물","URL주소"])

        #시그널-슬롯 연결         
        self.tableWidget.doubleClicked.connect(self.doubleClicked)

    def setTableWidgetData(self):
        row = 0
        for n in range(0,10):
            #클리앙의 중고장터 주소 
            url ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
            data = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(data, 'html.parser')
            list = soup.find_all('a', attrs={'class':'list_subject'})

            f = open("clien.txt", "a+", encoding="utf-8")
            for item in list:
                try:
                    span = item.find("span", attrs={"class":"subject_fixed"})
                    title = item.text.strip()
                    #라인에디터에 입력된 문자열 받아서 검색
                    if (re.search(self.lineEdit.text(), title)):
                        title = title.replace("\t", "")
                        title = title.replace("\n", "")
                        print(title)
                        link = 'https://www.clien.net'  + item['href'] 
                        print(link.strip())
                        f.write(title+"\n")
                        f.write(link + "\n")
                        #행데이터로 출력 
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(title))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(link))
                        row += 1
                        print("row: ", row) 
                except:
                    pass
             
            f.close()

    def doubleClicked(self):
        url = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        webbrowser.open(url) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myForm = DemoForm()
    myForm.show()
    app.exec_()



