import json

f = open("du_lieu/ho_ten.json", encoding='utf-8')
noi_dung = json.load(f)
f.close()
noi_dung_bo_sung = {"So dien thoai": "1234556", "Email":"abc@gmail.com"}

noi_dung.update(noi_dung_bo_sung)
f = open("du_lieu/ho_ten.json", 'w', encoding='utf-8')
json.dump(noi_dung, f, indent=4, ensure_ascii=False)