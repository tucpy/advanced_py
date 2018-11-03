from quan_ly_giao_dich_update_json import *
import time
from datetime import datetime
import json

print("Quản lý giao dịch:")
list_vang = []
list_tien = []
tiep_tuc = 1
while tiep_tuc == 1:        
    ma = input("Nhập mã GD:\t")
    ngay = input("Nhập ngày GD:\t")
    
    so_luong = int(input("Nhập số lượng:\t"))
    
    i = int(input("Chọn loại giao dịch: 1: Vàng, 2: Tiền Tệ:\t"))
    if i==1:
        tong_slv = 0
        tong_tien_vang = 0
        loai = input("Chọn loai: 18k / 24k / 9999:\t")
        don_gia = eval(input("Nhập đơn giá:\t"))
        gdv = GiaoDich(ma, ngay, don_gia, so_luong, loai)
        list_vang.append(gdv)
        for item in list_vang:
            tong_slv += item.so_luong
            tong_tien_vang += item.thanh_tien()
            print(item.in_giao_dich())        
        print("Tổng số lượng:", tong_slv)
        print("Tổng số tiền:", tong_tien_vang)
    if i==2:
        tong_slt = 0
        tong_tien_tien = 0
        loai = input("Chọn loai: USD / EUR / AUD:\t")
        don_gia = eval(input("Nhập tỷ giá:\t"))
        mua = True
        gd = int(input("Bạn mua hay bán? 1: mua, 0: bán:\t"))
        if gd == 0:
            mua = False 
        gdtt = GiaoDichTienTe(ma, ngay, don_gia, so_luong, loai, mua)
        list_tien.append(gdtt)
        for item in list_tien:
            tong_slt += item.so_luong
            tong_tien_tien += item.thanh_tien()
            print(item.in_giao_dich())        
        print("Tổng số lượng:", tong_slt)
        print("Tổng số tiền:", tong_tien_tien)
    
    tiep_tuc = int(input("Bạn muốn tiếp tục giao dịch? 1: Có, 0: Không\t")) 
        
ghi_file = eval(input("Ban co muon ghi file JSON? 1. Co, 0: Khong\t"))

'''
#Cach 1
if ghi_file == 1:
    data ={}
    data['giao_dich_vang'] = []
    for item in list_vang:
        data['giao_dich_vang'].append({
            'ma': item.ma,
            'ngay':item.ngay,
            'don_gia':str(item.don_gia),
            'so_luong':str(item.so_luong),
            'loai':str(item.loai)
        })
    data['giao_dich_tien'] =[]
    for item in list_tien:
        data['giao_dich_tien'].append({
            'ma': item.ma,
            'ngay':item.ngay,
            'don_gia':str(item.don_gia),
            'so_luong':str(item.so_luong),
            'loai':str(item.loai),
            'mua': str(item.mua)
        })
    
    ngay_hh = datetime.now()
    ten_luu = ngay_hh.strftime("%Y-%m-%d-%H-%M-%S") 
    ten_tap_tin = ten_luu + ".json"
    f = open(ten_tap_tin,'w')
    json.dump(data,f,indent=4)
    f.close()
    print("Da ghi noi dung vao tap tin:", ten_tap_tin)
'''

#Cach 2
if ghi_file == 1:
    noi_dung_ghi={}
    noi_dung_ghi['giao_dich_vang']=[]
    noi_dung_ghi['giao_dich_tien_te']=[]
    for item in list_vang:
        noi_dung_ghi['giao_dich_vang'].append(item.__dict__)
    for item in list_tien:
        noi_dung_ghi['giao_dich_tien_te'].append(item.__dict__)
    
    ngay_hh = datetime.now()
    ten_luu = ngay_hh.strftime("%Y-%m-%d-%H-%M-%S")
    ten_luu+=".json"
    path_luu="du_lieu/"+ten_luu
    f = open(path_luu,'w')
    json.dump(noi_dung_ghi,f,indent=4, ensure_ascii=False)
    f.close()
    print("Da ghi file")