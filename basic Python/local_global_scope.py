balance=3050

def scope_check(price):
    #balance-=price  Error here
    global balance
    balance-=price
    return balance



print(scope_check(100))
print(balance)