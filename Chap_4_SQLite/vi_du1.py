'''
Tao db qlNhanVien voi table PHONG
'''


import sqlite3
conn = sqlite3.connect('sqlite_db/qlNhanVien.db')
sql = '''
CREATE TABLE PHONG (
 id INTEGER PRIMARY KEY,
 ten TEXT NOT NULL UNIQUE,
 chuc_nang TEXT NOT NULL
);'''

conn.execute(sql)
conn.commit()
conn.close()