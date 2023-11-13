person={

    'Name':"Md. Rahim Uddin",
    'Age' :28,
    'District':'Feni',
    'Designation' :'Engineer'
}
#print(person)
person['University']='DUET'
#print(person)

# for key,value in person.items():
#     print(f"{key} : {value}")

for index,key in enumerate(person.items()):
    print(index,key)
