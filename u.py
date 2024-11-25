import sqlite3
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class StudentTable(QWidget):
    def __init__(self):
        super().__init__()

        # Kết nối tới cơ sở dữ liệu
        self.conn = sqlite3.connect('example.db')
        self.cursor = self.conn.cursor()

        # Lấy dữ liệu từ bảng HocSinh
        self.cursor.execute("SELECT * FROM HocSinh")
        self.data = self.cursor.fetchall()

        # Tạo QTableWidget và điền dữ liệu
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(len(self.data))
        self.table_widget.setColumnCount(5)  # Số cột của bảng HocSinh
        self.table_widget.setHorizontalHeaderLabels(['Mã Số', 'Tên Học Sinh', 'Ngày Tháng Năm Sinh', 'Tuổi', 'Ghi Chú'])

        for row_idx, row_data in enumerate(self.data):
            for col_idx, item in enumerate(row_data):
                self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

        # Kết nối sự kiện chỉnh sửa ô
        self.table_widget.itemChanged.connect(self.update_database)

        # Thiết lập bố cục và thêm QTableWidget vào cửa sổ chính
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    def update_database(self, item):
        row = item.row()
        column = item.column()
        value = item.text()

        # Lấy Mã Số của học sinh trong hàng hiện tại
        maso = self.table_widget.item(row, 0).text()

        # Tạo câu lệnh cập nhật cho cột tương ứng
        columns = ['MaSo', 'TenHocSinh', 'NgayThangNamSinh', 'Tuoi', 'GhiChu']
        column_name = columns[column]

        # Kết nối tới cơ sở dữ liệu và cập nhật giá trị
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute(f"UPDATE HocSinh SET {column_name} = ? WHERE MaSo = ?", (value, maso))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = StudentTable()
    window.show()
    sys.exit(app.exec_())
