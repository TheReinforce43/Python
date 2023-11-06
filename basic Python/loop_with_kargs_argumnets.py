def customized_name(first,last,**addition):
    for key,value in addition.items():  
          print(key," : ",value)
    name=f"{first}  {" "}  {last}"
    return name
f_name=input("Enter your first name : ")
l_name=input("Enter your last name : ")
title_name=input("Enter your title : ")
versity_name=input("Enter your University : ")
District=input("Enter your district : ")

Personal_name=customized_name(first=f_name,last=l_name,title=title_name,University=versity_name,District=District)
print(Personal_name)
    
