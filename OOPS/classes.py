class Student:
    name:str = ""
    email:str = ""
    age:int = 0

    def display(self):
        print(f"Name : {self.name} Email : {self.email} Age : {self.age}")

s1 = Student()

s1.name = "Vansh"
s1.email = "vansh@gmail.com"
s1.age = 23

s1.display()