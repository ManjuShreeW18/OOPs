class Student:
    def __init__(self,name,roll,age):
        self.name=name  #dont frget to put the access modfiers
        self._roll=roll
        self.__age=age

    def get_age(self): #get ki only return
        return self.__age
    
    def set_age(self,num):
        if num<45:  #Set lo logic undali
            self.__age=num
            print("u r eligible")
        else:
            
            print("u r not eligible")

    def get_roll(self):
        return self._roll
    def set_roll(self,no):
        if no>0:
            return self._roll
        else:
            print("something went wrong")

s1=Student("manju",7,21)
print(s1.get_age())
print(s1.get_roll())

s1.set_age(23)
print(s1.get_age())

