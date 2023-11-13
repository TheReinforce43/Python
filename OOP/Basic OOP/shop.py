class shop:

    item=[]
    def __init__(self,buyer):
        self.buyer=buyer
    def add_item(self,product):
        self.item.append(product)

person1=shop('Farhan')
person1.add_item('pen')
person1.add_item('Shoes')
print(person1.item)

person2=shop('Karim')
person2.add_item('Books')
person2.add_item('Mobile')
print(person2.item)