# Abstraction
from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
     pass  # Must Usable


class Triangle(Shape):
    def area(self):
       area = 0.5 * self.dim1 * self.dim2
       print("Area Of A Triangle = " , area)


class Rectangle(Shape):
    def area(self):
       area =self.dim1 * self.dim2
       print("Area Of A Rectangle = " , area)

t = Triangle(20,30)
t.area()
r = Rectangle(20,30)
r.area()