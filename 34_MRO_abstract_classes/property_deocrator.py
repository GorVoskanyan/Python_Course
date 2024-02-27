class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance    # private attribute
    
    @property
    def balance(self):
        return self.__balance 
    
    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance
        
        
account1 = BankAccount('Alex', 50000)
# print(account1.get_balance())   
# account1.set_balance(100000)
# print(account1.get_balance())   

# print(account1.balance)
# account1.balance = 100000
# print(account1.balance)


