class Payment:
    def pay(self, payment_method:str, amount:int):
        if payment_method == "Credit Card":
            print(f"Paying amount : {amount} with {payment_method}")
        elif payment_method == "Debit Card":
            print(f"Paying amount : {amount} with {payment_method}")
        elif payment_method == "UPI":
            print(f"Paying amount : {amount} with {payment_method}")

payment = Payment()
payment.pay("Credit Card", 30000)
payment.pay("Debit Card", 30000)
payment.pay("UPI", 30000)