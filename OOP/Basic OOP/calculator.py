class calculator:

    def add(self,num1,num2):
        return num1+num2
    def subtract(self,num1,num2):
        return num1-num2
    def multiply(self,num1,num2):
        return num2*num1
    def divide(self,num1,num2):

        try:
            result=num1/num2
        except ZeroDivisionError:
            print("Zero Division error here")
            result=None
        finally:
            return result
        
    
a=int(input("Enter First value : "))
b=int(input("Enter second value : "))

my_calculator=calculator()
print("sum two value : ",my_calculator.add(a,b))
print("subtract two value : ",my_calculator.subtract(a,b))
print("multiply two value : ",my_calculator.multiply(a,b))
print("Dividation two values : ", my_calculator.divide(a,b))