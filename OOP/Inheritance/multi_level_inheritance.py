class Vehicle:

    def __init__(self,Name,Price) -> None:
        self.Name=Name
        self.Price=Price
    
    def __repr__(self) -> str:
        return f"Name : {self.Name} Price : {self.Price} "

class Bus(Vehicle):

    def __init__(self,Name,Price,Seat) -> None:
        super().__init__(Name,Price)
        self.Seat=Seat
    def __repr__(self) -> str:
        return super().__repr__()
    
class Truck(Vehicle):
    def __init__(self,Name,Price,Weight) -> None:
        super().__init__(Name,Price)
        self.Weight=Weight
    def __repr__(self) -> str:
        return super().__repr__()
    
class ACBus(Bus):
    def __init__(self, Name, Price, Seat,Temparature) -> None:
        super().__init__(Name, Price, Seat)
        self.Temparature=Temparature
    def __repr__(self) -> str:
        return f"Name :{self.Name} Price={self.Price} Seat={self.Seat} Temparature={self.Temparature}"

# StarLine=Bus('Star Line',150000,30)
EnaAc=ACBus('Ena',23423,30,'15 Degree')
# print(StarLine)
print(EnaAc)



    
        
