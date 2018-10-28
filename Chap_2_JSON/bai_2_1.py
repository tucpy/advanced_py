import urllib.request
import json

chuoi_url = "http://dev-er.com/service_api_ban_sach/api_service_sach.php"

url = urllib.request.urlopen(chuoi_url)

data = json.loads(url.read().decode())

print(data)

print("Tong so sach:", len(data))
print("Danh sach sach")
i=1
for item in data:
    print(i, '/',item['ten_sach'],'Ngay xuat ban:',item['ngay_xuat_ban'],'Gia bia',item['gia_bia'])
    i += 1