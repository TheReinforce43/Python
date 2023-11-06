# def full_name(first,last):
#     name=first+' '+last
#     return name
# #maintain sequence order parameter
# print(full_name("Rahim",'Uddin'))
# #Not maintain sequence order parameter
# frst=input("Enter the first name  : ")
# lst=input("Enter the second name : ")

# FullName=full_name(last=lst,first=frst)
# print(FullName)


# def Personal_name(first,last,**addition):
#     name=f"{title} {first} {last} {addition} "
#     print(addition)
#     return name

# first=input("Enter your first name : ")
# last=input("Enter your last name : ")
# title=input("Enter your title : ")
# addition=input("Enter additional information : ")

# customized_name=Personal_name(last=last,first=first,title=title,addition=addition)

# print(customized_name)

def famous_name(first,last,**addition):
    print(addition)
    name=f"{ addition['title']} {first} {last} {addition['District']}"
    return name

first=input("Enter Your first name : ")
last=input("Enter your last name : ")
title=input("Enter your title : ")
District=input("Enter you District : ")

Personal_Intro=famous_name(first=first,last=last,title=title,District=District)
print(Personal_Intro)