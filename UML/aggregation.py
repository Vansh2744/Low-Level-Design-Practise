class Student:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

class Department:
    def __init__(self, name:str):
        self.name = name
        self.students:list[Student] = []

    def add_student(self, std:Student):
        self.students.append(std)

    def show_students(self):
        for std in self.students:
            print(f"Name : {std.name} and Age : {std.age} and Department : {self.name}")

std1 = Student("Vansh", 23)
std2 = Student("Aman", 20)
std3 = Student("Kartik", 24)
std4 = Student("Rohan", 22)

dpt1 = Department("CSE")
dpt1.add_student(std1)
dpt1.add_student(std2)
dpt1.add_student(std3)

dpt1.show_students()

dpt2 = Department("Robotics")
dpt2.add_student(std3)
dpt2.add_student(std4)
dpt2.add_student(std2)

dpt2.show_students()

del dpt2
print(std1.name)