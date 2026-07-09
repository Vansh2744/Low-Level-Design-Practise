from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self):
        pass

class WithdrawableAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    @abstractmethod
    def withdraw(self):
        pass

class SavingAccount(WithdrawableAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs {amount} Deposited, Current Balance : {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
             self.balance -= amount
             print(f"Rs {amount} Credited, Current Balance : {self.balance}")
        else:
            print(f"Not Emough Amount, balance is {self.balance}")

class FixedDepositAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs {amount} Deposited, Current Balance : {self.balance}")

save = SavingAccount(3000)
save.deposit(1000)

save.withdraw(2000)

fixed_depo = FixedDepositAccount(3000)
fixed_depo.deposit(5000)