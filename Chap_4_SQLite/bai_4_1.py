import sqlite3
from product import *

tiep_tuc = 1

while tiep_tuc:
    print("Ban muon lam gi?")
    print("1: Hien thi danh sach san pham")
    print("2: Tim kiem san pham theo ten")
    print("3: Cap nhat san pham")
    print("4: Them san pham moi")
    print("5: Xoa san pham")

    chon = int(input("Vui long chon chuc nang: "))
    if chon == 1:
        dsSanPham = DocDanhSachSanPham()
        #print(dsSanPham)
        if len(dsSanPham) > 0:
            for item in dsSanPham:
                print('Ma san pham', item[0],', ten san pham', item[1])
        else:
            print('Khong co san pham nao')
    
    elif chon == 2:
        giatriTim = input('Nhap ten can tim: ')
        dsSanPham = TimKiemSanPham(giatriTim)
        if len(dsSanPham) > 0:
            for item in dsSanPham:
                print('Ma san pham', item[0], ',ten san pham', item[1])
        else:
            print('Khong co san pham nao')

    elif chon == 3:
        id = int(input('Cho biet Ma san pham can cap nhat: '))
        sp = DocSanPham(id)
        if sp != None:
            tensp = str(input("Nhap ten san pham: "))
            don_gia = float(input("Nhap don gia moi: "))
            so_luong = int(input("Nhap so luong moi: "))
            sp = {'name':tensp, 'price': don_gia, 'amount': so_luong, 'id': id}
            
            if CapNhatSanPham(sp)==1:
                print('Da cap nhat')
            else:
                print('Cap nhat ko thanh cong')
        else:
            print('Khong ton tai san pham co ma nay')

    elif chon == 4:
        tensp = str(input("Nhap ten san pham: "))
        don_gia = float(input("Nhap don gia: "))
        so_luong = int(input("Nhap so luong: "))
        sp={'name':tensp, 'price': don_gia, 'amount': so_luong}
        n = ThemSanPham(sp)
        if n>=1:
            print('Da them thanh cong')
        else:
            print('Them khong thanh cong')
        
    elif chon == 5:
        id = int(input('Cho biet Ma san pham can xoa:'))
        sp = DocSanPham(id)
        if sp!= None:
            if XoaSanPham(id)==1:
                print("Da xoa")
            else:
                print('Xoa khong thanh cong')
        else:
            print('Khong ton tai san pham co ma nay')
        
    
    else:
        print('Vui long chi chon cac gia tri trong danh sach')
    tiep_tuc = int(input("Ban co muon tiep tuc khong? (1: tt)"))
    
        
