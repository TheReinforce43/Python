class person:

    def __init__(self,name,age,height) -> None:
        self.person_name=name
        self.age=age
        self.height=height
    
    def Eat(self):
        print("Eating food like as Normal person")

    def Excercise(self):
        raise NotImplementedError


class Cricketer(person):

    def __init__(self, name, age, height,YoYo_score) -> None:
        super().__init__(name, age, height)
        self.YoYo_score=YoYo_score
    
    def Eat(self):
        print("Eat Not fetable food")

    def Excercise(self):
        return f"{self.person_name} maintain his practice"
    def __add__(self,others):
        return self.age + others.age
    def __sub__(self,others):
        return self.YoYo_score - others.YoYo_score
    def __gt__(self,others):
        return self.YoYo_score > others.YoYo_score

    def __len__(self):
        return int(self.YoYo_score)

Shakib=Cricketer('Shakib',38,5.7,17.5)
Mushi=Cricketer('Mushfiq',38,5.5,18.3)
# Shakib.Eat()
print(Shakib.Excercise())
print(f"total age {Shakib.person_name} and {Mushi.person_name} =",Shakib+Mushi)
print(f"Difference of YoYo score =","{:.3f}".format(Shakib-Mushi))
greater_yoyo_score=Shakib >Mushi
if greater_yoyo_score :
    print ( f"{Shakib.person_name} has more yoyo score then {Mushi.person_name}")
else:
    print ( f"{Shakib.person_name} has less yoyo score then {Mushi.person_name}")

print(f"strength of {Shakib.YoYo_score} :",len(Shakib))