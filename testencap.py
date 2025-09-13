class encap:
    def __init__(self,name,balance,deposit):
        self.name=name  #using access modifiers
        self._balance=balance
        self.__deposit=deposit

    def get_name(self):
        print(f"name:{self.name}")

    def set_name(self,new_name):

        if isinstance(new_name,str):
            self.new_name=new_name
        else:
            print("invalid inout")

    def get_balance(self):
        return self._balance
    
    def set_balance(self,num):
        
        if num>=0:
            self._balance=num
            print("the balance is ",self._balance)
        else:
            print("invalid balance")

    def get_deposit(self):
        return self.__deposit
    def set_deposit(self,amount):

        if amount>=100:
            self.__deposit=amount
            self._balance+=amount
            print("balance",self._balance)
        else:
            print("min amount is 100")

e1=encap("manju",100000,1000)
e1.get_name()
print(e1.get_balance())
print(e1.get_deposit())

e1.set_deposit(2000)
e1.get_balance()




