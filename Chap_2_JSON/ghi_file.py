import json

noi_dung = {"Ho ten":"Nguyen Van A", "Dia chi":"Nguyen Chi Thanh"}
f = open("du_lieu/ho_ten.json", 'w')
json.dump(noi_dung, f,indent = 4, ensure_ascii=False)
f.close()
