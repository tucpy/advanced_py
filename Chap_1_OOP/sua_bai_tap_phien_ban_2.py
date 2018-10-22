import abc


class Hinh:
    __metaclass__ = abc.ABCMeta

    def __init__(self, ten):
        self.ten = ten

    @classmethod
    @abc.abstractmethod
    def Tinh_DT(self):
        return 0

    @classmethod
    @abc.abstractmethod
    def Tinh_CV(self):
        return 0

    def __str__(self):
        return "Hình: "+self.ten + "\nDT:" + \
            str(self.Tinh_DT()) + "\nCV:"+str(self.Tinh_CV())

class Hinh_tron(Hinh):
    def __init__(self, ten, r):
        Hinh.__init__(self, ten)
        self.r = r

    def Tinh_DT(self):
        return 3.1416 * self.r * self.r

    def Tinh_CV(self):
        return 2*3.1416*self.r




class Hinh_chu_nhat(Hinh):
    def __init__(self, ten, d, r):
        Hinh.__init__(self, ten)
        self.d = d
        self.r = r

    def Tinh_DT(self):
        return self.d*self.r

    def Tinh_CV(self):
        return 2*(self.d+self.r)



# test
htron = Hinh_tron("Hình tròn tâm O", 2.3)
hcn = Hinh_chu_nhat("Hình chữ nhật ABCD", 10, 5)
print(htron)
print("\n")
print(hcn)
