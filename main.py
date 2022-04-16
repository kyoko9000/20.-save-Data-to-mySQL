#no need to install anything
import sys
# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
# just change the name
from gui import Ui_MainWindow

# pip install mysql.connector-python
import mysql.connector

class MainWindow:
    def __init__(self):
        # the way app working
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # khai bao button *****************************************
        self.uic.Button_load_data.clicked.connect(self.show_data)
        self.uic.Button_update.clicked.connect(self.save_data)

    def show_data(self):
        try:
            # clear error on the screen
            self.uic.textEdit_data.setText('')
            # read text from combobox database
            choose_database = self.uic.comboBox_chosse_database.currentText()
            print(choose_database)

            # read text from combobox table
            choose_table = self.uic.comboBox_choose_table.currentText()
            print(choose_table)

            # connect to mysql*********************
            db = mysql.connector.connect(user='root', password='1234',
                                         host='127.0.0.1', database=choose_database)

            # command to choose table custom
            code_8 = 'SELECT * FROM {}'.format(choose_table)
            mycursor = db.cursor()  # create mycoursor
            mycursor.execute(code_8)  # execute command
            result = mycursor.fetchall()  # result
            print(result)

            # load du lieu lên tablewidget ************
            a = 0
            for row in result:
                a = len(row)
            self.uic.tableWidget.setRowCount(len(result))  # tao so row
            self.uic.tableWidget.setColumnCount(a)  # tao so column

            # fill data to tablewidget
            for row_number, row_data in enumerate(result):
                for column_number, data in enumerate(row_data):
                    self.uic.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except:
            self.uic.textEdit_data.setText("no data")
            print("no data")

    def save_data(self):
        # tim ra toa doa cua item can thay the
        currentItems = 0
        for currentItems in self.uic.tableWidget.selectedItems():
            print('row: ', currentItems.row())
            print("column: ", currentItems.column())
            print("value: ", currentItems.text())
        try:
            db = mysql.connector.connect(user='root', password='1234',
                                         host='127.0.0.1', database="new_database")

            ID_value = self.uic.tableWidget.item(currentItems.row(), 0).text()
            print("ID: ", ID_value)
            # take value
            row_val = currentItems.text()
            row_po = ID_value

            if currentItems.column() == 2:
                sql = "UPDATE `customer` SET `age`= %s WHERE `ID` = %s"
                val = (row_val, row_po)
                mycursor = db.cursor()  # run command
                mycursor.execute(sql, val)
                db.commit()
                print(mycursor.rowcount, "record(s) affected")

            elif currentItems.column() == 1:
                sql = "UPDATE `customer` SET `Name`= %s WHERE `ID` = %s"
                val = (row_val, row_po)
                mycursor = db.cursor()  # run command
                mycursor.execute(sql, val)
                db.commit()
                print(mycursor.rowcount, "record(s) affected")

            elif currentItems.column() == 3:
                sql = "UPDATE `customer` SET `address`= %s WHERE `ID` = %s"
                val = (row_val, row_po)
                mycursor = db.cursor()  # run command
                mycursor.execute(sql, val)
                db.commit()
                print(mycursor.rowcount, "record(s) affected")
        except:
            print("no data")


    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())