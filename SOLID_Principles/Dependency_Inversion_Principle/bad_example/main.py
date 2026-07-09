from notification_service import NotificationService

notify = NotificationService()
notify.send_by_email("Hello Vansh")
notify.send_by_sms("Credited Rs 3000/-")