# python
Chapter 2 - JSON:
Mục tiêu chính:
- Làm việc với dữ liệu JSON từ API trên Internet: đọc, hiển thị nội dung 
- Làm việc với tập tin .json: đọc, hiển thị, ghi tập tin .json


Note:
JSON syntax:
- Dữ liệu theo định dạng "name" : value
- Dữ liệu phân cách bằng dấu phẩy
- Curly brace {} chứa các đối tượng
- Square bracket [] chứa các mảng

Các kiểu dữ liệu hỗ trợ: string, number, object(JSON object), array, boolean, null. Không hỗ trợ các kiểu: function, date, undefined

- Các bước làm việc với JSON:
+ Đọc dữ liệu JSON từ internet:
B1: mở url dẫn đến nơi chứa nội dung
url = urllib.request.urlopen("tên đường dẫn")
B2: đọc dữ liệu từ url-> decode dữ liệu. Sau đó dùng loads() để parse dữ liệu JSON
data = json.loads(url.read().decode())
B3: xử lý dữ liệu theo yêu cầu
vd: in dữ liệu định dạng JSON(import pprint)
pprint(data)

Nếu nội dung theo định dạng UNICODE, khai báo DEFAULT_ENCODING = 'utf-8'

+ Đọc dữ liệu JSON từ tập tin JSON:
B1: mở tập tin JSON
f = open(filename, encoding='utf-8')
B2: dùng phương thức load() để parse dữ liệu JSON từ tập tin đã mở
data = json.load(data file)
B3: xử lý dữ liệu
vd: pprint(data)
B4: ghi dữ liệu vào tập tin .json
f= open("tên_tập_tin.json","w")
json.dump(dữ liệu theo định dạng json, f[, indent = 4])

+ Ghi dữ liệu vào tập tin .json: ghi thêm (append)
B1: chuẩn bị dữ liệu thêm mới (theo định dạng item mới kiểu JSON)
B2: mở tập tin .json nguồn, load dữ liệu ra
B3: gọi phương thức update(dữ liệu thêm mới) để đưa dữ liệu mới vào
B4: mở tập tin .json nguồn/đích theo chế độ ghi
B5: gọi phương thức dump() để ghi dữ liệu vào tập tin .json

Vd: 
company = {"name": "ABC", "address":"xyz"}
list = []
list.append(company)
new = {"company" : list}

f = open('people.json')
data = json.load(f)
data.update(new)

f = open('people.json', 'w')
json.dump(data, f, indent=4)

Bài tập:
1. read_json_from_internet.py 
2. read_json_from_internet_noi_bat.py
3. read_json_file_thong_ke.py
4. quan_ly_giao_dich.py
5. them_phong_karaoke.py