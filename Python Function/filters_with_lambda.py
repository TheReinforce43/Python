actors = [
    {'name':'Shakib Khan','age':50},
    {'name':'Amin Khan','age':57},
    {'name':'Abdur Razzak','age':80},
    {'name':'Riaz','age':45},
    {'name':'Ilias Kanchon','age':68}

]
Elders=filter(lambda actor:actor['age']>50,actors)
Not_fibers=filter( lambda actor : actor['age']%5!=0,actors)
# print(list(Elders))
# print(tuple(Elders))
print(list(Not_fibers))