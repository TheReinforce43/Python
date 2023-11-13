class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name
        self._branch='Dhaka'
        self.__current_deposit=initial_deposit
    
    def add_deposite(self,amount):
        # self.current_deposit+=amount   # public Access Modifiers
        self.__current_deposit+=amount   #Convert Private Access Modifiers
    def get_balance(self):
        return self.__current_deposit
    
DBBL=Bank('Rahim Uddin',10000)
DBBL.add_deposite(20000)
# DBBL.current_deposit=0
# print(DBBL.current_deposit)  # Can't access due to private access modifiers
print(DBBL.get_balance())

print(DBBL._branch)
DBBL._branch='Rangpur'
print(DBBL._branch)
