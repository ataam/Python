from abc import ABC, abstractmethod
class Shape():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    @abstractmethod
    def calculateAre(self):
        pass
    @abstractmethod
    def Info(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
            super().__init__(width,height)
    def calculateArea(self):
        return self.width * self.height
    def Info(self):
        print(f"Width: {self.width} and Height {self.height} of that shape")
rec1=Rectangle(10,124)
print(rec1.calculateArea())
rec1.Info()

