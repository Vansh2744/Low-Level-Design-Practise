class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher:
    def std_info(self, obj):
        print(f"Name of the student is : {obj.name} and Age of the student is : {obj.age}")

std = Student("Vansh",23)
teach = Teacher()
teach.std_info(std)