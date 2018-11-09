import re
dia_chi_email = input('Cho biet dia chi email: ')
matchObj = re.match(r'^[A-Z0-9._%+=]+@[A-Z0-9.-]+\.[A-Z]{2,}$', dia_chi_email, re.M|re.I)

if matchObj:
    print('Hop le')
else:
    print(dia_chi_email, 'khong hop le')