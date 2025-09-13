# single parent multipe childs

class Human:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"hi {self.name} and age is {self.age}")

class Male(Human):

    def __init__(self, name, age,location):
        Human.__init__(self,name,age)
        # super().__init__(name, age)
        self.location=location

    def show(self):
        print(f"{self.name} {self.location}")

class Woman(Human):

    def __init__(self, name, age,address):
        super().__init__(name, age)
        self.address=address

    def show(self):
        print(f"{self.name} {self.age} {self.address}")

w1=Woman("manju",21,"tel")
m1=Male("jessi",23,"hyd")
w1.show()
m1.show()


        