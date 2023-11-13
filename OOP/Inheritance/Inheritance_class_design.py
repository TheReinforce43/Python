class Device:

    def __init__(self,brand,price,color) -> None:
        self.brand=brand
        self.price=price
        self.color=color
    def run(self):
        return f"Run very well, {self.brand}"

class Laptop(Device):

    def __init__(self, brand, price, color,memory) -> None:
        super().__init__(brand, price, color)
        self.memory=memory
    def __repr__(self) -> str:
        return f"{self.brand} {self.color} {self.price} {self.memory}"
class Camera(Device):

    def __init__(self, brand, price, color,pixel) -> None:
        super().__init__(brand, price, color)
        self.pixel=pixel
    def __repr__(self) -> str:
        return f"{self.brand} {self.color} {self.price} {self.pixel}"

class Phone(Device):
    def __init__(self, brand, price, color,dual_sim) -> None:
        super().__init__(brand, price, color)
        self.dual_sim=dual_sim
    def __repr__(self) -> str:
        return f"{self.brand}{self.color}{self.price}{self.dual_sim}"

hp=Laptop('hp',50000,'Black','500GB')
print(hp)
# print(hp.run())