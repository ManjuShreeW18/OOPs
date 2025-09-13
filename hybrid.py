class Father:
    def eat(self):
        print("eats")

    def sleep(self):
        print("he sleeps")

class Child(Father):

    def eat(self):
        print("eats fast")

class Mother:

    def eat(self):
        print("hi")

class Son(Father,Mother):

    def eat(self):
        print("ican eat faster")
        super().eat()

s1=Son()
s1.eat()
print(Son.mro()) #to confirm
