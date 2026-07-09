from notification_service import NotificationService
from email_service import EmailService
from sms_service import SMSService


email = EmailService()
sms = SMSService()
notify_email = NotificationService(email)
notify_sms = NotificationService(sms)
notify_email.notify("Hello Vansh")
notify_sms.notify("Credited Rs 3000/-")