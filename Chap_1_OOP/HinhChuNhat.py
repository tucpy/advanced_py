class HinhChuNHat():
    def __init__(self, _cd, _cr):
        self.chieudai = _cd
        self.chieurong = _cr
    def chuvi(self):
        return (self.chieudai + self.chieurong)*2
    def dientich(self):
        return (self.chieudai * self.chieurong)

if __name__ =="__main__":
    cd,cr = eval(input('chieu dai, chieu rong: '))
    hcn = HinhChuNHat(cd,cr)

    chuvi = hcn.chuvi()
    chuvi1 = HinhChuNHat.chuvi(hcn)
    print("Chu vi: %i" %chuvi)
    print("Chu vi: %i" %chuvi1)

    dientich = hcn.dientich()
    print("Dien tich: %i" %dientich)

