'''
Xuat du lieu cua database SQL de check lai trong Python
(Neu ko dung phan mem DB browser for SQLite)
'''


import sqlite3
conn = sqlite3.connect('sqlite_db/qlNhanVien.db')
chuoiSQL = 'select * from PHONG'
cursor = conn.execute(chuoiSQL)
for item in cursor:
    print(item[1])#neu chi muon lay field thu 1 trong tuple
    print(item)

conn.close()