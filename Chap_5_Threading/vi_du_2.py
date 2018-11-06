import _thread
import time

def tinh_tong(gt):
    tong = 0
    chuoi=''
    for i in range(1,gt+1):
        tong+=i
        chuoi+= str(i) + ''
        if i%2==0:
            print('i = ', chuoi)
            thong_bao()
            time.sleep(1)