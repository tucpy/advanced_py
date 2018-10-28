import json
import urllib.request

def read_json_from_internet_unicode(url1):
    DEFAULT_ENCODING = 'utf-8'   
    
    urlResponse = urllib.request.urlopen(url1)
    
    if hasattr(urlResponse.headers, 'get_content_charset'):
        encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
    else:
        encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING
    
    noi_dung = json.loads(urlResponse.read().decode(encoding))
    return noi_dung

if __name__=="__main__":
    chuoiUrl='http://dev-er.com/service_api_ban_sach/api_service_sach.php?task=sach_noi_bat'
    noi_dung = read_json_from_internet_unicode(chuoiUrl)
    print(noi_dung)
    print("---Danh sach %d sach noi bat---" %(len(noi_dung)))

    i = 1
    for item in noi_dung:
        print(i,'/',item['ten_sach'],'Tac gia:',item['ten_tac_gia'])
        print('- Ngay xuat ban:', item['ngay_xuat_ban'],'\t','Gia bia:', item['gia_bia'])
        
        #In 200 ki tu dau trong phan gioi thieu
        sum_gioi_thieu = item['gioi_thieu']
        #print(sum_gioi_thieu[:200])
        print('- Gioi thieu:', sum_gioi_thieu[:200])
        i += 1





