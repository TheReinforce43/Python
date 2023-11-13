
from math import pi

class Shape:

    def __init__(self,name) -> None:
        self.shape_name=name
    def area(self):
        pass

class Square(Shape):

    def __init__(self, name) -> None:
        super().__init__(name)

    def area(self,x):
        return x*x 
class Rectangle(Shape):

    def __init__(self, name) -> None:
        super().__init__(name)

    def area(self,x,y):
        return x*y


class Circle(Shape):

    def __init__(self, name) -> None:
        super().__init__(name)
    
    def area(self,x):
        return pi*(x**2)
    

sqr=Square('square')
print(sqr.area(10))

rect=Rectangle('rect')
print(rect.area(10,20))

crcl=Circle('crck')
print(crcl.area(10))

print(issubclass(Square,Shape))
print(isinstance(rect,Rectangle))