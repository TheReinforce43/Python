class student:

    def __init__(self,name,current_class,id):
        self.name=name
        self.current_class=current_class
        self.id=id
    def __repr__(self):
        text=(f"Name : {self.name } Roll: {self.id} current_class={self.current_class}")
        return text
    
class teacher:
    def __init__(self,name,subject,id) -> None:
        self.teacher_name=name
        self.subject=subject
        self.teacher_id=id
    def __repr__(self) -> str:
        text=f"teacher_name : {self.teacher_name}, subject {self.subject} and his id :{self.teacher_id}"
        return text
    
class school:

    def __init__(self,name) -> None:
        self.school_name=name
        self.teachers=[]
        self.students=[]
 
    def add_teacher(self,name,subject):
        id=len(self.teachers)+101
        Teacher=teacher(name,subject,id)
        self.teachers.append(Teacher)
    def add_student(self,name,fee):

        if fee < 6500 :
            return f"Unable to ennrollig"
        else :
            id=len(self.students)+1
            Student=student(name,'Math',id)
            self.students.append(Student)
            return f"{name} is enrolling and with id : {id} and {fee-6500} he will get"

    def __repr__(self) -> str:
        print("whelcome to ",self.school_name)
        print("-----Our Teachers-----")
        for teacher in self.teachers:
            print(teacher)
        print("-----Our Students-----")

        for student in self.students:
            print(student)
        
        return "We conclusion our introduction"

    
phitron=school('Phitron')
phitron.add_student('Rahim Uddin',6000)
phitron.add_student('Rahim Uddin',6500)
phitron.add_student('Hasnat Real',8009)
phitron.add_student('Mahmud Pias',6503)

phitron.add_teacher('Dr.Abul Kashem','Software Design')
phitron.add_teacher('Dr.Nasim Akhtar','Database')
phitron.add_teacher('Mahbub Alam','Operating System')

print(phitron)




