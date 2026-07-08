from user import User
from report_generator import ReportGenerator
from email_service import EmailService
from user_repo import UserRepository

user = User("Vansh","vansh@gmail.com")
user_db = UserRepository()
e_ser = EmailService()
report = ReportGenerator()

user_db.save(user)
e_ser.send_email(user)
report.generate_report(user)