from abc import abstractmethod
from abc import ABC

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        print(f"Area of Rectangle : {self.length*self.breadth}")

    def perimeter(self):
        print(f"Perimeter of Rectangle : {2*(self.length+self.breadth)}")

class Square(Shape):
    def __init__(self, s):
        self.side = s

    def area(self):
        print(f"Area of Circle : {self.side*self.side}")

    def perimeter(self):
        print(f"Perimeter of Circle : {4*(self.side)}")

rec = Rectangle(10, 20)
rec.area()
rec.perimeter()

sq= Square(5)
sq.area()
sq.perimeter()