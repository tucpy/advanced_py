import threading
import time


class tinh_tong_chan (threading.Thread):
    def __init__(self, gt):
        threading.Thread.__init__(self)
        self.gt = gt
        self.tong = 0
        self.chuoi = ''
    def run(self):
        print("Thuc hien tinh tong cac so chan")
        sum_chan(self,self.gt)
        print("Tong cac so chan tu 1 den", self.gt," = ", self.tong)

def sum_chan(self,gt):
    for i in range(1, self.gt+1):
        if i%2==0:
            self.tong+=i
            self.chuoi += str(i) + ' '
            print(self.chuoi)
            time.sleep(0.5)

class tinh_tong_le (threading.Thread):
    def __init__(self, gt):
        threading.Thread.__init__(self)
        self.gt = gt
        self.tong = 0
        self.chuoi = ''
    def run(self):
        print("Thuc hien tinh tong cac so le")
        sum_le(self,self.gt)
        print("Tong cac so le tu 1 den", self.gt," = ", self.tong)
    
def sum_le(self,gt):
    for i in range(1, self.gt+1):
        if i%2!=0:
            self.tong+=i
            self.chuoi += str(i) + ' '
            print(self.chuoi)
            time.sleep(0.5)


if __name__ == "__main__":
    thread_chan = tinh_tong_chan(10)
    thread_le = tinh_tong_le(10)
    print("==========>", threading.activeCount())
    thread_chan.start()
    thread_le.start()
    print("==========>__", thread_le.getName())
    thread_chan.join()
    thread_le.join()
    print("ok")