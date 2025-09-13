from abc import ABC,abstractmethod
import math as m
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("area of circle: ")
        print( m.pi*self.radius*self.radius)
    
class Rect(Shape):
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid

    def area(self):
        print("area :")
        print(self.len*self.wid)

c1=Circle(4)
c1.area()
r1=Rect(2,3)
r1.area()        
        
        