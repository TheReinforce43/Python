import random as rn
lst=[]
for _ in range(10):
    lst.append(rn.randint(1,100))
# print(lst)
highest=max(lst)
lowest=min(lst)
print(highest,lowest,len(lst))
