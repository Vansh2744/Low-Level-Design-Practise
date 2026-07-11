from notification_channel import NotificationChannel

class NotificationService:
    def __init__(self, service:NotificationChannel):
        self.service = service

    def notify(self, message):
        self.service.send(message)
