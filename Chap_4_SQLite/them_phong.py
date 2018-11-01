'''
Them du lieu trong table PHONG
'''


import sqlite3
conn = sqlite3.connect('sqlite_db/qlNhanVien.db')
sql = 'insert into PHONG(id, ten, chuc_nang) values(?,?,?)'

'''
Nhap tung dong

conn.execute(sql,(1,'Hanh chinh','Giai quyet cac cong viec hanh chinh cua cty'))
conn.commit()
conn.close()
'''

'''
Neu muon nhap hang loat
'''
for i in range(1,10):
    conn.execute(sql,(i+1,'Hanh chinh' + str(i),'Giai quyet cac cong viec hanh chinh cua cty' + str(i)))
    conn.commit()
conn.close()
