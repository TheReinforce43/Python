# with open('message.txt','w') as file:
#     file.write('I love you , python\n')
#     file.write('Osthir befar shefar\n')

# with open('message.txt','a') as file:
#     file.write('Bangladesh Won the toss and elect to bowl first\n')

with open('message.txt','r') as file:
    text=file.read()
    print(text)