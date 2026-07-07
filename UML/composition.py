class Student:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

class Department:
    def __init__(self, name:str, std_name:str, std_age:int):
        self.name = name
        self.std_obj = Student(std_name, std_age)

    def show_students(self):
        print(f"Name : {self.std_obj.name} and Age : {self.std_obj.age} and Department : {self.name}")

dpt = Department("CSE", "Vansh", 23)
dpt.show_students()