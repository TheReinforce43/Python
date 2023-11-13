class shop:

    market='jamuna'

    def __init__(self,buyer) -> None:
        self.buyer=buyer
        self.cart=[]

    def add_to_cart(self,item):
        self.cart.append(item)

    def print_cart(self):

        for value in self.cart:
            print(value,end=' ') 

person1=shop('Farhan')
person1.add_to_cart('Book')
person1.add_to_cart('Pen')
# person1.print_cart()
person2=shop('Karim')
person2.add_to_cart('Mobile')
person2.add_to_cart('laptop')
person2.print_cart()
