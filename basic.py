class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"name: {self.name}")

p=Person("manju")
p.show()
