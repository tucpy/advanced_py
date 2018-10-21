class PTBN():
    def __init__(self, _a, _b):
        self.a =_a
        self.b =_b
    def NghiemPT(self):
        nghiem =''
        if self.a == 0 and self.b != 0:
            nghiem ="Phuong trinh vo nghiem"
        elif self.a == 0 and self.b == 0:
            nghiem ="Phuong trinh vo so nghiem"
        else:
            nghiem = -self.b/self.a
        return nghiem
    def in_nghiem(self):
        print("Ket qua: ", self.NghiemPT())

if __name__=="__main__":
    a, b = eval(input("Nhap a, b: "))
    x = PTBN(a,b)
    #Cach 1
    nghiem = x.NghiemPT()
    print("Nghiem x: ", nghiem)
    #Cach 2
    nghiem1 = x.in_nghiem()
    
    #Kiem tra thuoc tinh cua doi tuong
    pt = PTBN(5,3)
    if hasattr(pt,'a'):
        print(getattr(pt,'a'))