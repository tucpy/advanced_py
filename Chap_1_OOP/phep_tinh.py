class pheptinh():
    def __init__(self, _a, _b):
        self.a = _a
        self.b = _b
    def Tong(self):
        return a + b
    def Hieu(self):
        return a - b
    def Tich(self):
        return a*b
    def Thuong(self):
        return a/b

if __name__ =="__main__":
    a,b = eval(input("Nhap a, b: "))
    x = pheptinh(a,b)
    print("Tong: ", x.Tong())
    print("Hieu: ", x.Hieu())
    print("Tich: ", x.Tich())
    print("Thuong: ", x.Thuong())