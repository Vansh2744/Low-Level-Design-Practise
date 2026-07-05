class Student:
    name:str = ""
    email:str = ""
    age:int = 0

    def display(self):
        print(f"Name : {self.name} Email : {self.email} Age : {self.age}")

s1 = Student()
s2 = Student()

s1.name = "Vansh"
s1.email = "vansh@gmail.com"
s1.age = 23

# s1.display()
# s2.display()

class Movie:
    name : str = "Avengers"
    total_seats : int = 10
    ticket_price : int = 20
    booked_seats : int = 0

    def book_ticket(self, seats):
        if self.total_seats >= seats:
            self.total_seats -= seats
            self.booked_seats += seats
            print("Seat booked")

        else:
            print("Sorry not enough seats available")

    def show_status(self):
        print(f"Movie : {self.name}  Seats Available : {self.total_seats}  Seats Booked : {self.booked_seats} ")

obj = Movie()

obj.show_status()
obj.book_ticket(5)
obj.show_status()
obj.book_ticket(5)
obj.show_status()
obj.book_ticket(5)