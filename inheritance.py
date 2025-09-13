# Single
class Parent:
    def __init__(self):
        print("hihihi")

    def work(self):
        print("can work")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("hello")

    def work(self):
        print("cant wrk")

c1=Child()
print(c1.work())
