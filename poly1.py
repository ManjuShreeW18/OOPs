# method overriding example

# same method name and also sam enumber of arguments

class Bird:

    def fly(self):
        print("i can fly")

class Penguin(Bird):

    def fly(self):
        print("i cant fly")
        super().fly()

# b1=Bird()
# b1.fly()
p1=Penguin()
p1.fly()

# another example
class Father:
    def sleep(self):
        print("sleep timings:10 to 8")

    def eat(self):
        print("can eat")

class Daughter(Father):
    def sleep(self):
        print("sleep timings: 11 tp 5")
        super().sleep()

d1=Daughter()
d1.sleep()
# f1=Father()
# f1.sleep()
