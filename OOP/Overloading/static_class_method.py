class static_test:

    person_name=[]  #static attribute
    cnt=0   #static attribute
    def __init__(self,name) -> None:
        self.person_name.append(name)
        self.cnt+=1
    @staticmethod
    def static_add(a,b):
        return a+b
    
    @classmethod

    def count_instance(cls):
        return cls.cnt

test=static_test('Farhan')
test=static_test('Farhan')
print(static_test.count_instance())
print(static_test.static_add(10,13))
print(test.static_add(10,13))


