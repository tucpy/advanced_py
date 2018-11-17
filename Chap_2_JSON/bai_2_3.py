import json

f = open('files/QLCT_1.json', encoding='utf-8')
data = json.load(f)
Cty = data['CONG_TY']
Dvi = data['DON_VI']

print(Cty)
print(Dvi)

for item in Cty:
    print("Ten cong ty:", item['Ten'])
    print("Dia chi: ", item['Dia_chi'])
    print("Tong so nhan vien:")

print("--- Thong ke so nhan vien theo don vi ---")
i = 1
for item in Dvi:
    print(i, '/', "Ten don vi:", item['Ten'])
    print("\t","-","So nhan vien:", item['So_Nhan_vien'])
    print("\t", "-","Ty le:", item['Ty_le'])
    i+=1

def doc_noi_dung_json(filename):
    data_file = open(filename, encoding='utf-8')
    data = json.load(data_file)
    data_file.close()
    return data

data_new = doc_noi_dung_json('files/QLCT_2.json')

cty_new = data_new['CONG_TY']
print("SDT", cty_new['Dien_thoai'],"Mail",cty_new['Mail'])

dvi_new = cty_new['DON_VI']
for item in dvi_new:
    print('Ten:', item['Ten'])
    print('So nhan vien:',item['So_Nhan_vien'],'\n')
