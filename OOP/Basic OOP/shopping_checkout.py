class shopping:

    def __init__(self,name) -> None:
        self.customer_name=name
        self.cart=[]
    
    def add_to_cart(self,item,price,quantity):
        product={'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)
    def checkout(self,give_money):
        partial_sum=0

        for value in self.cart:
            partial_sum+=value['price'] *value['quantity']
        ans=give_money-partial_sum
        return ans

t=int(input("How much customer enter in shoping mall : "))
for _ in range(t):

    My_shopping=shopping('Rahim Uddin')
    My_shopping.add_to_cart('Headphone',2200,2)
    My_shopping.add_to_cart('Pen',10,2)
    My_shopping.add_to_cart('Book',300,5)
    money=int(input("Enter you paying money : "))
    # My_shopping.checkout(1000)
    pre_calculation=My_shopping.checkout(money)
    print(f"Dear {My_shopping.customer_name} Sir/madam, ")
    if(pre_calculation==0): print(" thanks sir for you pay exact money")
    elif(pre_calculation>0): print(f"Sir, You will get {pre_calculation} taka")
    else : print(f"sir, you need to pay {pre_calculation} taka")


