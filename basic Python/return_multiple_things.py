def multiple(a,b):
    sum=a+b
    mul=a*b
    subtract=abs(a-b)
    print("call inside in own method")
    # return sum,mul,subtract
    return [sum,mul,subtract]

sum,mul,subtract=multiple(100,200)
print(sum,mul,subtract)
