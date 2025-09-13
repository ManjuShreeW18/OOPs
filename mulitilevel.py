class Grand:
    def __init__(self):
        print("hi ")

    def walk(self):
        print("i walk slowly")

class Father(Grand):
    def __init__(self):
        print("hellooooo")
        super().__init__()

    def walk(self):
        print("i can walk normaly")

class Child(Father):

    def walk(self):
        print("i can walk fast")
        super().walk()

c1=Child()
c1.walk()

