class person:

    def __init__(self,name,age,money) -> None:
        self.person_name=name
        self._age=age
        self.__money=money
    
    #using getter
    @property
    def get_money(self):
        return self.__money
    
    #using setter
    @get_money.setter
    def get_money(self,amount):
        if amount<  0: return 'Negave amount can\'t be added' 
        else :
            self.__money+=amount
        # return self.__money

farhan=person('farhan',28,12232)
# print(farhan.get_money())

#Using getter
print("Before using setter",farhan.get_money)
farhan.get_money=12432
print("After using setter",farhan.get_money)
