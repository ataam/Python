class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def calculateArea(self):
        return self.width * self.height

Rec1 = Rectangle(5,5)
print(Rec1.width,Rec1.height)
print(f"Area of Rec1: {Rec1.calculateArea()} cm")
print(""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>""")
Rec2 = Rectangle(50234,4325)
print(Rec2.width,Rec2.height)
print(f"Area of Rec2: {Rec2.calculateArea()} cm")



