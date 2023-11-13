import random 
nums=[]

for _ in range(10):
    nums.append(random.randint(1,100))
print(nums)

# for value in nums:
#     if value%2==1 and value%5==0 :
#         print(value)


comprehensions=[value for value in nums if value%2==1 if value%5==0]
print(comprehensions)