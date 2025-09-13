from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("barks")

class Cat(Animal):
    def sound(self):
        print("meow")

d=Dog()
c=Cat()
d.sound()
c.sound()