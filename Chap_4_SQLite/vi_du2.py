'''
Tao db qlNhanVien voi table NHAN_VIEN
'''


import sqlite3
conn = sqlite3.connect('sqlite_db/qlNhanVien.db')

sql = '''CREATE TABLE NHAN_VIEN(
 id INTEGER PRIMARY KEY,
 ho_ten TEXT NOT NULL,
 tuoi INTEGER NOT NULL,
 dia_chi TEXT NOT NULL,
 luong REAL,
 phong_id INTEGER NOT NULL,
 FOREIGN KEY(phong_id) REFERENCES PHONG(id));'''



conn.execute(sql)
conn.commit()
conn.close()