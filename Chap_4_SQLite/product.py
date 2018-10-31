import sqlite3

def DocDanhSachSanPham():
    conn = sqlite3.connect('du_lieu/product.db')
    cursor=conn.execute('select id, name, price, amount from product')
    ds = cursor.fetchall()
    conn.close()
    return ds

def DocSanPham(id):
    conn = sqlite3.connect('du_lieu/product.db')
    cursor=conn.execute('select id, name, price, amount from product where id =?',(id,))
    ds = cursor.fetchone()
    conn.close()
    return ds

def ThemSanPham(sp):
    conn = sqlite3.connect('du_lieu/product.db')
    chuoiSQL='insert into product(name, price, amount) values(?,?,?)'
    cursor = conn.execute(chuoiSQL,(sp['name'],sp['price'],sp['amount'],))
    n = cursor.rowcount
    conn.commit()
    conn.close()
    return n

def CapNhatSanPham(sp):
    conn = sqlite3.connect('du_lieu/product.db')
    chuoiSQL='update product set name=?, price=?, amount=? where id=?'
    cursor = conn.execute(chuoiSQL,(sp['name'],sp['price'],sp['amount'],sp['id'],))
    n = cursor.rowcount
    conn.commit()
    conn.close()
    return n

def XoaSanPham(id):
    conn = sqlite3.connect('du_lieu/product.db')
    chuoiSQL='Delete from product where id=?'
    cursor = conn.execute(chuoiSQL,(id,))
    n = cursor.rowcount
    conn.commit()
    conn.close()
    return n

def TimKiemSanPham(gt):
    BieuThucDieuKien = '%' + gt + '%'
    conn = sqlite3.connect('du_lieu/product.db')
    cursor=conn.execute('select id, name, price, amount from product where name like?', (BieuThucDieuKien,))
    ds = cursor.fetchall()
    conn.close()
    return ds



