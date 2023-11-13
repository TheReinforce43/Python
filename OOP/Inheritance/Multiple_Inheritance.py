class Family:

    def __init__(self,address) -> None:
        self.address=address
class School:

    def __init__(self,id,school_name) -> None:
        self.school_id=id
        self.school_name=school_name

class Sports_club:

    def __init__(self,club_id,club_name) -> None:
        self.club_id=club_id
        self.club_name=club_name
class Student(Family,School,Sports_club):
    def __init__(self,Name, address,id,school_name,club_id,club_name) -> None:
       Family.__init__(self,address)
       School.__init__(self,id,school_name)
       Sports_club.__init__(self,club_id,club_name)
       self.student_name=Name
    def __repr__(self) -> str:
        return f" Name: {self.student_name} School: {self.school_name}"
    
Student1=Student('Md. Rahim Uddin','Feni',101,'ATS','club-1','Bondhon')
print(Student1)