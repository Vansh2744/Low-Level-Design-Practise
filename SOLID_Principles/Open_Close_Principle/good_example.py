from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPIMethod(Payment):
    def pay(self, amount):
        print(f"Paying amount : {amount} with UPI")

class CreditCardMethod(Payment):
    def pay(self, amount):
        print(f"Paying amount : {amount} with Credit Card")

class DebitCardMethod(Payment):
    def pay(self, amount):
        print(f"Paying amount : {amount} with Debit Card")

class PaymentProcessor:
    def process_payment(self, payment:Payment, amount):
        payment.pay(amount)

upi = UPIMethod()
credit = CreditCardMethod()
debit = DebitCardMethod()

processor = PaymentProcessor()

processor.process_payment(upi, 30000)
processor.process_payment(credit, 60000)
processor.process_payment(debit, 45000)