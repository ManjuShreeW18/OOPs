from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print('area of rectangle is ')
        return self.length * self.width
    
    
r1=rectangle(6,5)

print(r1.area())
