class Laptop:

    def __init__(self,brand,price,color,memory) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.memory=memory
    def run(self):
        return f"Running very well"
    def working_perspective(self):
        return f"Learning and earning with coding"

class Mobile:
    def __init__(self,brand,price,color,dual_sim) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.dual_sim=dual_sim
    def run(self):
        return f"Running very well on mobile perspective"
    def phone_call(self):
        return f"Phone call coming from twice sim is {self.dual_sim} "
class Camera:
    def __init__(self,brand,price,color,pixel) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.pixel=pixel
    def run(self):
        return f"Running very well on Camera perspective"
    def change_lens(self):
        return f"change lens very comfortably"
    
hp=Laptop('hp',50000,'Black','500GB')
print(hp.run())