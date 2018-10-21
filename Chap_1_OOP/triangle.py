from polygon import *
#Neu khong bo cac lenh ben polygon vao main, thi khi goi class trong triangle, cac lenh do se duoc thuc thi
print("Tinh cv, dt tam giac")

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    
    def find_area(self):
        a, b, c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print("The area of the triangle is %.2f" %area)

    def find_perimeter(self):
        a, b, c = self.sides
        perimeter = a + b + c
        print("The perimeter of the triangle is %.2f" %perimeter)
    #Overriding Method from Polygon
    def display_sides(self):
        print("Triangle has 3 sides:")
        Polygon.display_sides(self)

if __name__ == "__main__":
    triangle = Triangle()
    triangle.input_sides()
    triangle.find_area()
    triangle.find_perimeter()
    

