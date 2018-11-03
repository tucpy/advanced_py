import json
from pprint import pprint

print("Nhap thong tin phong karaoke")
id1 = input("Nhap ID:\t")
ten = input("Nhap ten:\t")
ma_so = input("Nhap ma so:\t")
id_loai_phong = input("Nhap ID loai phong (1 hoac 2 hoac 3):\t")
don_gia = input("Nhap don gia:\t")
so_khach_toi_da = input("Nhap so khach toi da:\t")
trang_thai = input("Nhap trang thai (CON TRONG hoac CO KHACH):\t")

phong = {"ID": id1, "Ten": ten, "Ma_so": ma_so, "ID_LOAI_PHONG": id_loai_phong, "Don_gia": don_gia, "So_khach_toi_da":so_khach_toi_da, "Trang_thai": trang_thai}

list1 = []
list1.append(phong)
new = {ma_so:list1}

f = open('du_lieu/quan_ly_phong_karaoke.json', encoding ='utf-8')
data = json.load(f)
data.update(new)
f.close()

f = open('du_lieu/quan_ly_phong_karaoke.json', 'w', encoding ='utf-8')
json.dump(data,f, indent=4)
f.close()
print("Da ghi xong")

f = open('du_lieu/quan_ly_phong_karaoke.json', encoding ='utf-8')
data = json.load(f)
pprint(data)