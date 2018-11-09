import re
ten_file = input('Nhap ten tap tin hinh anh: ')
matchObj = re.match(r'^([A-Z0-9._%+-]{3,})+(\.(jpeg|png|gif|bmp))$', ten_file, re.M|re.I)
# 2 nhom: (nhom 1: ki tu bat ki) (nhom 2: .jpeg|.png....)

if matchObj:
    print('Hop le')
else:
    print(ten_file, 'khong hop le')