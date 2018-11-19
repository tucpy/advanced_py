import pdb
def tinh_bmi(can_nang, chieu_cao):
    return can_nang/(chieu_cao*chieu_cao)
def danh_gia_bmi(bmi):
    if bmi<18.5:
        return 'Gay'
    elif bmi<24.99:
        return 'Binh thuong'
    else:
        return 'Thua can'

can_nang = eval(input("can nang: "))
chieu_cao = eval(input("chieu cao: "))

pdb.set_trace()
bmi = tinh_bmi(can_nang, chieu_cao)
danh_gia = danh_gia_bmi(bmi)
print(bmi)
print(danh_gia)