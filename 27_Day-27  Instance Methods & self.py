# Manipulating properties securely inside execution boundaries
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

account = BankAccount("Alex", 100.0)
print(account.deposit(50.0))
