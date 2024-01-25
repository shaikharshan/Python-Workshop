class student:
    def __init__(self,name,age,cgpa):
        self.name=name
        self.age=age
        self.cgpa=cgpa
class course:
    def __init__(self,course_name,max):
        self.course_name=course_name
        self.max=max
        self.students=[]
    def add_student(self,student):
        if len(self.students)<self.max:
            self.students.append(student)
    def view_student(self):
        for student in self.students:
            print(i.student)
c1=course("pyshop",60)
s1=student("arshan",19,7)


            