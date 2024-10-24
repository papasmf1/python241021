import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# 데이터베이스 처리를 위한 클래스
class ProductDatabase:
    def __init__(self, db_name="ProductList.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self._connect_db()

    def _connect_db(self):
        if not os.path.exists(self.db_name):
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            self._create_table()
        else:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()

    def _create_table(self):
        self.cursor.execute(
            "CREATE TABLE Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
        )
        self.connection.commit()

    def add_product(self, name, price):
        self.cursor.execute("INSERT INTO Products (Name, Price) VALUES(?,?);", (name, price))
        self.connection.commit()

    def update_product(self, prod_id, name, price):
        self.cursor.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", (name, price, prod_id))
        self.connection.commit()

    def delete_product(self, prod_id):
        self.cursor.execute("DELETE FROM Products WHERE id=?", (prod_id,))
        self.connection.commit()

    def get_all_products(self):
        self.cursor.execute("SELECT * FROM Products;")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


# UI 처리를 위한 클래스
class DemoForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Chap10_ProductList.ui", self)
        
        self.db = ProductDatabase()

        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

        # 이벤트 연결
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.double_click)

        # 버튼 클릭 시그널 연결
        self.pushButton.clicked.connect(self.addProduct)
        self.pushButton_2.clicked.connect(self.updateProduct)
        self.pushButton_3.clicked.connect(self.removeProduct)
        self.pushButton_4.clicked.connect(self.getProduct)

    def addProduct(self):
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db.add_product(name, price)
        self.get_products()

    def updateProduct(self):
        prod_id = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db.update_product(prod_id, name, price)
        self.get_products()

    def removeProduct(self):
        prod_id = self.prodID.text()
        self.db.delete_product(prod_id)
        self.get_products()

    def getProduct(self):
        self.tableWidget.clearContents()
        products = self.db.get_all_products()

        row = 0
        for item in products:
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)
            
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))

            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

            row += 1

    def double_click(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

    def closeEvent(self, event):
        self.db.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
