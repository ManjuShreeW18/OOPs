class Father:
    def __init__(self,name):
        self.name=name

    def work(self):
        print(f"my name is {self.name} and i owrk")

class Mother:
    def __init__(self,age):
        self.age=age
        print(f"my age is {self.age}")

    def work(self):
        print("i work daily")

class Son(Father,Mother):

    def __init__(self, name, age):

        Father.__init__(self, name)
        Mother.__init__(self, age)

    def work(self):
        print("This is son's work")
        super().work()


s1=Son("sridhar",45)
s1.work()
    