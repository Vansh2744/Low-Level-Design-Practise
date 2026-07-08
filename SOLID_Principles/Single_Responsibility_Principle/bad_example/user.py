class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        print(f"Saving {self.name} to Database")

    def send_email(self):
        print(f"Sending Email to {self.email}")

    def generate_report(self):
        print(f"Generating report of {self.name}")