import sqlite3
# 1 tạo database có tên 2.database.db
file_path = 'C:/Users/PC/Desktop/google drive link/2.database.db'
conn = sqlite3.connect(file_path)
#                ------------------------------
# Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
cursor = conn.cursor()

# 2. tạo bảng table tên hocsinh
# # Tạo bảng HocSinh với MaSo là khóa chính và cột NgayThangNamSinh
# cursor.execute('''
# CREATE TABLE HocSinh (
#     MaSo TEXT PRIMARY KEY,
#     TenHocSinh TEXT,
#     NgayThangNamSinh DATE,
#     Tuoi INTEGER,
#     GhiChu TEXT
# )
# ''')
#
# # Lưu thay đổi và đóng kết nối
# conn.commit()
# conn.close()
#
# print("Bảng HocSinh đã được tạo thành công.")

# Dữ liệu của 5 em học sinh

# 3. nhập dữ liệu đầu tiên là danh sách các học sinh vào table đã tạo
students = [
    ('HS001', 'Nguyen Van A', '2005-05-12', 18, ''),
    ('HS002', 'Tran Thi B', '2006-07-24', 17, ''),
    ('HS003', 'Le Van C', '2005-11-30', 18, ''),
    ('HS004', 'Pham Thi D', '2007-02-15', 16, ''),
    ('HS005', 'Doan Van E', '2006-09-20', 17, '')
]

# Ghi dữ liệu vào bảng HocSinh
cursor.executemany('''
INSERT INTO HocSinh (MaSo, TenHocSinh, NgayThangNamSinh, Tuoi, GhiChu)
VALUES (?, ?, ?, ?, ?)
''', students)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("Dữ liệu của 5 em học sinh đã được ghi vào bảng HocSinh.")

