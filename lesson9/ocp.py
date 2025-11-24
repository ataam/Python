from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius,diameter):
        self.diameter = diameter
        self.radius = radius
    def area(self):
        return self.radius * self.diameter


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width


class AreaOfShape:
    def calculateArea(self,shape):
        return shape.area()

c = Circle(5, 10)
r = Rectangle(4, 6)

calc = AreaOfShape()
print(calc.calculateArea(c))  # площа кола
print(calc.calculateArea(r))