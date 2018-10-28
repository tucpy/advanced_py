import abc
import math

class Hinh(abc.ABC):
    @abc.abstractmethod
    def tinh_chu_vi(self):
        pass
    @abc.abstractmethod
    def tinh_dien_tich(self):
        pass

class HinhTron(Hinh):
    def __init__(self, r):
        self.r = r
    def tinh_chu_vi(self):
        return 2 * self.r * math.pi
    def tinh_dien_tich(self):
        return math.pi * math.pow(self.r, 2)


class HinhChuNhat(Hinh):
    def __init__(self, cd, cr):
        self.cd = cd
        self.cr = cr
    def tinh_chu_vi(self):
        return (self.cd + self.cr) * 2
    def tinh_dien_tich(self):
        return self.cd * self.cr

class HinhTamGiac(Hinh):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    #if((self.a+self.b>self.c)and(self.a+self.c>self.b)and(self.b+self.c>self.a)and(self.a>0)and(self.b>0)and(self.c>0))
    def tinh_chu_vi(self):
        return self.a + self.b + self.c
    def tinh_dien_tich(self):
        self.p = (self.a+self.b+self.c)/2
        return math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))



if __name__=="__main__":
    hinhtron = HinhTron(20)
    print("Chu vi hinh tron:",hinhtron.tinh_chu_vi())
    print("Dien tich hinh tron:",hinhtron.tinh_dien_tich())

    hinhchunhat = HinhChuNhat(5,10)
    print("Chu vi hinh chu nhat:", hinhchunhat.tinh_chu_vi())
    print("Dien tich hinh chu nhat:", hinhchunhat.tinh_dien_tich())

    hinhtg = HinhTamGiac(5,10, 12)
    print("Chu vi hinh tam giac:", hinhtg.tinh_chu_vi())
    print("Dien tich hinh tam giac:", hinhtg.tinh_dien_tich())



    
        
        
    