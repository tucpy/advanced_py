class PTbac2():
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def phuong_trinh_bac_hai(self):
        if (self.a == 0):
            if self.b == 0:
                if self.c != 0:
                    print("Phuong trinh vo nghiem")
                else:
                    print("Phuong trinh co vo so nghiem")
            else:
                x = -self.c/self.b
                print("Phuong trinh co nghiem: x=", x)
        else:
            delta = self.b*self.b - 4*self.a*self.c
            if delta < 0:
                print("Phuong trinh vo nghiem")
            elif delta ==0:
                x = -self.b/2*self.a
                print("Phuong trinh co nghiem kep: x= ", x)
            else:
                x1 = (-self.b + math.sqrt(delta))/(2*self.a)
                x2 = (-self.b - math.sqrt(delta))/(2*self.a)
                print("Phuong trinh co 2 nghiem phan biet")
                print("x1: ", x1)
                print("x2: ", x2)

if __name__ =="__main__":
    a,b,c = eval(input('a, b, c: '))
    ptb2 = PTbac2(a,b,c)
    nghiem = ptb2.phuong_trinh_bac_hai()
