# ************************** man hinh loai 2 *************************
import sqlite3
import sys

import openpyxl
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gui1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.header_list = None
        self.file_path = None
        self.cursor = None
        self.conn = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.pushButton.clicked.connect(self.load_data)
        self.uic.pushButton_4.clicked.connect(self.choose_data)

    def load_data(self):
        self.file_path = 'C:/Users/PC/Desktop/google drive link/2.database.db'
        # Kết nối tới cơ sở dữ liệu
        self.conn = sqlite3.connect(self.file_path)
        self.cursor = self.conn.cursor()

        # Lấy dữ liệu từ bảng HocSinh
        self.cursor.execute("SELECT * FROM HocSinh")
        data = self.cursor.fetchall()
        # Tạo QTableWidget và điền dữ liệu
        self.uic.tableWidget.setRowCount(len(data))
        self.uic.tableWidget.setColumnCount(5)  # Số cột của bảng HocSinh
        self.header_list = ['Mã Số', 'Tên Học Sinh', 'Ngày Tháng Năm Sinh', 'Tuổi', 'GhiChu']
        self.uic.tableWidget.setHorizontalHeaderLabels(self.header_list)

        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                if item is None:
                    item = ""
                self.uic.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

        # Đóng kết nối
        self.conn.close()

        # Kết nối sự kiện chỉnh sửa ô
        self.uic.tableWidget.itemChanged.connect(self.update_database)

    def update_database(self, item):
        row = item.row()
        column = item.column()
        value = item.text()

        # Lấy Mã Số của học sinh trong hàng hiện tại
        maso = self.uic.tableWidget.item(row, 0).text()

        # Tạo câu lệnh cập nhật cho cột tương ứng
        columns = ['MaSo', 'TenHocSinh', 'NgayThangNamSinh', 'Tuoi', 'GhiChu']
        column_name = columns[column]

        # Kết nối tới cơ sở dữ liệu và cập nhật giá trị
        conn = sqlite3.connect(self.file_path)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE HocSinh SET {column_name} = ? WHERE MaSo = ?", (value, maso))
        print(f"thông tin dã được lưu trữ vào database với:\n"
              f"       mã số: {maso}\n"
              f",column name: {column_name}\n"
              f",    giá trị: {value}")
        conn.commit()
        conn.close()

    def choose_data(self):
        selected_items = self.uic.tableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            # data at choose cell
            choose_data = []
            for col in range(self.uic.tableWidget.columnCount()):
                item = self.uic.tableWidget.item(row, col)
                if item:
                    choose_data.append(item.text())

            list_data = [self.header_list, choose_data]
            self.export_to_excel(list_data)
        else:
            print("Không có ô nào được chọn")

    def export_to_excel(self, data):
        # Chuyển đổi giá trị tại vị trí 0 và 3 ra dạng int
        data[1][3] = int(data[1][3])
        print("data", data)

        # # Lưu dữ liệu vào worksheet
        # file_path = 'export_data.xlsx'
        # workbook = openpyxl.Workbook()
        # sheet = workbook.active
        # for row in data:
        #     sheet.append(row)
        #
        # # Lưu workbook vào tệp Excel
        # workbook.save(file_path)
        #
        # print("Dữ liệu đã được lưu thành công vào tệp Excel.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
