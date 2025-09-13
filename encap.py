class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def get_balance(self):
        
        return self.__balance
    
    def set_balance(self,amount,name):
        if amount<=0:
            print("no balance")
            

        else:
            self.__balance=amount
            
            print(f"the balanace is: {amount}")

    def deposit(self,amount):
        if amount>=100:
            amount+=self.__balance
            print(f"balance {amount}")
        else:
            print("add min depoait amount")

b1=Bank("manju",100000)
print(b1.get_balance())
b1.deposit(456677)




        