#Ex-3 . Rectangle class that contains area() and perimeter() methods:
class Rectangle:
    def __init__(s,l,w):
        s.l = l
        s.w = w
        print("----Rectangle----")
    def Area(s):
        area = (s.l)*(s.w)
        print(f' Area      = {area}')
    def Perimeter(s):
        p = (2)*(s.l+s.w)
        print(f' Perimeter = {p}')
a = 15
b = 10
R = Rectangle(a,b)
R.Area()
R.Perimeter()
