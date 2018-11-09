import re

noi_dung = 'Cong hoa xa hoi chu nghia viet nam'
gia_tri_tim = input('Tim gi: ')
matchObj = re.search(r'.*' + gia_tri_tim + '(.*)', noi_dung, re.M|re.I)
# note: khong phan biet chu hoa chu thuong

if matchObj:
    print('Tim co')
else:
    print('Khong tim thay')