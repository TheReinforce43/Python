# from return_multiple_things import multiple

# result=multiple(10,20)
# print(result)

from return_multiple_things import multiple as ml

result=ml(30,50)
for key in result:
    print(key)