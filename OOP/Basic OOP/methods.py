class person:
    name='Md. Shah Karim Ullah'
    District='Feni'
    Feactures=['Graduate Person','Sub Assistent Engineer','CSE']
    def call(self):
        print("Call methods from class")
        print("call done")
    def send_sms(self,phone,sms):
        text=f"sms come from {phone} and message is : {sms}"
        return text


my_person=person()
# my_person.call()
result=my_person.send_sms(201203,'No more today')
print(result)