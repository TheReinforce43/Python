numbers=[10,2,35,43,64,36,86,36,84,25,97]

doubled=lambda num: num**2
print(numbers)
#double_nums=map(doubled,numbers)
double_nums=map(lambda num:num*2,numbers)
print(list(double_nums))