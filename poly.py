# method overloading how can we acheive

# a,b and a,b,c

class Calc:
    
    def add(self,*args):
        return sum(args)
            
        # total=0
        # for i in args:
        #     total+=sum
        # return total
    
    
c1=Calc()
print(c1.add(1,45,89,99,667))
    

    #function overloading
# This is a standalone function named 'add'
# It uses default values for parameters to simulate overloading
def add(a=0, b=0):
    print(a + b)

# Calling with no arguments
add()         # Output: 0

# Calling with one argument
add(5)        # Output: 5

# Calling with two arguments
add(3, 4)     # Output: 7


# method overoading

# This is a class with a method 'add'
# The method also uses default parameters to simulate overloading
class Calculator:
    def add(self, a=0, b=0):
        print(a + b)

# Create an object of the class
c = Calculator()

# Calling method with no arguments
c.add()         # Output: 0

# Calling method with one argument
c.add(10)       # Output: 10

# Calling method with two arguments
c.add(2, 3)     # Output: 5
