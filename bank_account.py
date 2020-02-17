class BankAccount:
   
    def __init__(self, bank_account_number, balance, int_rate, month_fee, customer):
        self.bank_account_number = bank_account_number
        self.balance = balance
        self.int_rate = int_rate
        self.month_fee = month_fee
        self.customer = customer

    def finish_month(self):
        int_amount = self.balance * self.int_rate / 12
        self.balance = self.balance + int_amount - self.month_fee
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

# bank_acc = BankAccount("1234567789",1000, 0.12, 50, "Harold")

# bank_acc.deposit(100)
# bank_acc.withdraw(300)

# print(bank_acc.finish_month())

# # print(bank_acc.balance)