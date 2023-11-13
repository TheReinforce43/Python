from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod  
    def eat(self):
        print("common eating behavior of Animal")

    def Move(self):
        print ("An animal can move")

class Monkey(Animal):

    def __init__(self,name) -> None:
        super().__init__()
        self.name=name
    def eat(self):
        print("Monkey can eat Banana")

class tiger(Animal):
    def __init__(self,name) -> None:
        super().__init__()
        self.name=name
    def eat(self):
        return f"{self.name} favourte meal is beef"

# tom=Monkey('tom')
# tom.eat()

Bangla_tiger=tiger('Royal Bengal Tiger')
print(Bangla_tiger.eat())

