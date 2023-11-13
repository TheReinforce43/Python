element='Jug','Mog','Glass','Pen','Khata'
print(element.count('Mog'))

if 'Khata' in element:
    print("exists")
else :
    print("Not Exists")

list_tuple=([1,2,3,4,5],(3,5,6,))
print(list_tuple[0][2])
list_tuple[0][2]=3434 #we can change the tuple when this are mutable data structure
print(list_tuple)
