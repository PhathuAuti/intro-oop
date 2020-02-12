class BankAccount:
   
    def __init__(self, balance, int_rate, month_fee):
        self.balance = balance
        self.int_rate = int_rate
        self.month_fee = month_fee
        self.int_amount = balance * int_rate / 12

    def finish_month(self):
        self.balance = int(self.balance + self.int_amount - self.month_fee)
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        self.balance = self.balance - amount

bank_acc = BankAccount(1000, 0.12, 50)

bank_acc.deposit(100)
bank_acc.withdraw(300)

print(bank_acc.finish_month())

# print(bank_acc.balance)
# print(bank_acc.bank_account_number)