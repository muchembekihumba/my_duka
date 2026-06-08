class BankAccount:
    def __init__(self, account_number, balance, owner_name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened
        self.is_closed = False

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner_name} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"{self.owner_name} withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"{self.owner_name}'s current balance: {self.balance}")

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Owner: {self.owner_name}")
        print(f"Balance: {self.balance}")
        print(f"Date Opened: {self.date_opened}")

    def close_account(self):
        self.balance = 0
        self.is_closed = True
        print(f"{self.owner_name}'s account {self.account_number} has been closed")


account1 = BankAccount("ACC001", 5000, "Alice", "2024-01-15")
account1.display_info()
account1.deposit(2000)
account1.withdraw(1000)
account1.check_balance()
account1.close_account()

print()

account2 = BankAccount("ACC002", 10000, "Bob", "2023-06-20")
account2.display_info()
account2.deposit(5000)
account2.withdraw(3000)
account2.check_balance()
account2.close_account()
