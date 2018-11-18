from thu_vien.quan_ly_sach import *
list_SGK = []
list_STK = []

tiep_tuc = 1
while tiep_tuc == 1:        
    ma = str(input("Nhap ma sach: "))
    ten = str(input("Nhap ten: "))
    ngay = input("Nhập ngày GD:")
    don_gia = int(input("Nhap don gia: "))
    so_luong = int(input("Nhap so luong: "))
    nxb = str(input("Nhap NXB: "))
    sach = Sach(ma,ten,ngay,don_gia,so_luong,nxb)
    
    loai_sach = eval(input("Day la sach giao khoa hay tham khao? 1: Giao khoa, 2: Tham khao:"))

    if loai_sach ==1:
        tinh_trang = eval(input("Sach cu hay moi? 1: Moi, 0: Cu :"))
        sach_gk = SachGiaoKhoa(ma,ten,ngay,don_gia,so_luong,nxb,tinh_trang)
        list_SGK.append(sach_gk)
        tong_tien = 0
        for item in list_SGK:
            print(item.in_sach())
            tong_tien += item.tinh_thanh_tien()
        print("Tong tien: ", tong_tien)
    else:
        thue = eval(input("Nhap thue: "))
        sach_tk = SachThamKhao(ma,ten,ngay,don_gia,so_luong,nxb,thue)
        list_STK.append(sach_tk)
        tong_tien = 0
        for item in list_STK:
            print(item.in_sach())
            tong_tien += item.tinh_thanh_tien()
        print("Tong tien: ", tong_tien)

