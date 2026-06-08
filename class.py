class Student:
    def __init__(self,name,age,student_no,course):
       self.name = name
       self.age = age
       self.student_no = student_no
       self.course = course

    def study(self, subject):
        print(f"{self.name} is studying {subject} in {self.course}")

    def introduce(self, greeting):
        print(f"{greeting}, I am {self.name}, I am {self.age} years old and my student number is {self.student_no}")

    def graduate(self, year):
        print(f"{self.name} has graduated from {self.course} in {year}")

student1 = Student("Alice", 20, "S001", "Computer Science")
print(student1.name, student1.age, student1.student_no, student1.course)
student1.introduce("Hello")
student1.study("Mathematics")
student1.graduate(2026)

student2 = Student("Bob", 22, "S002", "Business")
print(student2.name, student2.age, student2.student_no, student2.course)
student2.introduce("Hey")
student2.study("Economics")
student2.graduate(2027)