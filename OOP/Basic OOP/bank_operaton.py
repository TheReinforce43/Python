class bank:

    def __init__(self,amount) -> None:
        self.balance=amount
        self.min_withdraw=500
        self.max_withdraw=100000
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            print("You can't add negative amount of money")
    def withdraw(self,amount):
        if(amount < self.min_withdraw):
            print(f"Not possible to less than {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print (f"Not possible to more than {self.max_withdraw}")
        else :
            self.balance-=amount
            print(f"successully witdraw {amount} and current balance {self.balance}")
    def get_balance(self):
        return self.balance
dbbl=bank(100000)
dbbl.deposite(100)
# print(dbbl.get_balance())
# dbbl.deposite(-111)
dbbl.withdraw(1000)