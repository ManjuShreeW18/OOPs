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
    
