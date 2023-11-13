class phone:

    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price
    def print_value(self):
        print(f"owner : {self.owner} brand :{self.brand} price : {self.price}")
my_phone=phone('Rahim Uddin','Realme 10','18000')
your_phone=phone('Mustafizur Rahman','Apple 12',80000)
my_phone.print_value()
your_phone.print_value()