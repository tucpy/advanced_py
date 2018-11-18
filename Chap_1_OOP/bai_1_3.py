from thu_vien.CD import *

#Tao file CD.py nam trong folder thuvien

'''
# Cach 1
tiep_tuc = 1       
list_cd = []

while tiep_tuc == 1:
    ten = str(input("Nhap ten CD:"))
    ca_si = str(input("Nhap ten ca si:"))
    so_bai_hat = int(input("Nhap so bai hat:"))
    gia_thanh = float(input("Nhap gia thanh: "))
    cd = CD(ten,ca_si,so_bai_hat,gia_thanh)
    list_cd.append(cd)

    tiep_tuc = input("Ban co muon tiep tuc: 1")
    for item in list_cd:
        print(item.thong_tin_cd())
'''
# Cach 2

list_cd =[]
ten_cd = "1"
while ten_cd !="":
    ten_cd = str(input("Nhap ten CD:"))
    ca_si = str(input("Nhap ten ca si:"))
    so_bai_hat = int(input("Nhap so bai hat:"))
    gia_thanh = float(input("Nhap gia thanh: "))
    cd = CD(ten_cd,ca_si,so_bai_hat,gia_thanh)
    list_cd.append(cd)
    if len(list_cd) > 0: 
        for item in list_cd:
            print(item.thong_tin_cd())


