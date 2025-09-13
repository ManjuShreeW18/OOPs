class Dog:
    def bark(self):
        print("Woof!")

class Cat:
    def bark(self):
        print("Meow!")

def make_it_bark(animal):
    animal.bark()  # We only care if 'animal' can bark

dog = Dog()
cat = Cat()

make_it_bark(dog)  # Woof!
make_it_bark(cat)  # Meow!
