import re

# 1. Find date/time

text = u'Ngày 14/12/1996 là ngày 14/12 của năm 1996. Tháng 12/2000 là tháng cuối cùng của năm.'
datetime = '\d{1,2}\s?[:/-]\s?\d{1,2}\s?[:/-]\s?\d{4}'\
            '|\d{1,2}\s?[:/-]\s?\d{4}'\
            '|\d{1,2}\s?[:/-]\s?\d{1,2}'\
            '|\d{4}'

print (re.findall(datetime, text))

# 2. Email adress

text = u'địa chỉ mail của mình là xyz@gmail.com và 20172603@student.hust'
email = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+'

print(re.findall(email,text))

# 3. Link website
text = u'Đây là link bài viết mới nhất của mình trên viblo: https://viblo.asia/p/tro-chuyen-voi-le-viet-quocquoc-le-chuyen-gia-tri-tue-nhan-tao-phia-sau-su-thanh-cong-cua-google-automl-eW65GAW6ZDO'
url = 'https?:\/\/[^\s]*'
print (re.findall(url, text))

# 4. So thuc
text = "Mình nặng 70.5kg, nặng 175.8 cm."
digit = '\d+[\.,]\d+'

print(re.findall(digit, text))

# 5. Phan so

text = u'đạt được kết quả PES1 22/100 điểm'
fraction = '\d+\/\d+'

print (re.findall(fraction, text))

# 6. Chuan hoa tien te
text = u'mình có 2.000.000 yên trong tài khoản với hơn 2000$ tiền mặt mà k biết tiêu gì nên đổi hơn 10 tỷ vnđ ra đốt chơi.'
moneytag = [u'k', u'đ', u'ngàn', u'nghìn', u'usd', u'tr', u'củ', u'triệu', u'yên', u'tỷ']

for money in moneytag:
    text = re.sub(u'(^|\s)\d*([,.]?\d+)+\s*' + money, ' million ', text)
text = re.sub('((^|\s)(\d+\s*\$)|((^|\s)\$\d+\s*))', ' million ', text)

print (text)




