class Animal:

    def __init__(self) -> None:
        pass
    def sound(self):
        print("Animal make some sound")

class Dog(Animal):

    def __init__(self) -> None:
        super().__init__()

    def sound(self):
        print(f"Ghew Ghew")    
class Cow(Animal):

  def __init__(self) -> None:
      super().__init__()
      
  def sound(self):
        print(f"Hamba Hamba")  

    

class Cat(Animal):
    
    def __init__(self) -> None:
        super().__init__()
    def sound(self):
        print(f"Meow Meow")
    

Layka=Dog()
Buffelo=Cow()
jerry=Cat()

collection=[Layka,Buffelo,jerry]

for animal in collection:
    animal.sound()
