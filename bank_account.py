class BankAccount:
   
    def __init__(self, balance, int_rate, month_fee):
        self.balance = balance
        self.int_rate = int_rate
        self.month_fee = month_fee
        self.int_amount = balance * int_rate / 12

    def finish_month(self):
        self.balance = int(self.balance + self.int_amount - self.month_fee)
        return self.balance

    def deposit(self, plus_amnt):
        self.balance = self.balance + plus_amnt
    
    def withdraw(self, minus_amnt):
        self.balance = self.balance - minus_amnt

class Bank(BankAccount):
    pass

    def __init__(self, balance, int_rate, month_fee, bank_account_number):
        super().__init__(balance, int_rate, month_fee)
        self.bank_account_number = bank_account_number

#     def withdraw(bank_account_number,amount):

#     def deposit(bank_account_number,amount):

#     def transfer(from_bank_account_number,to_bank_account_number, amount):

bank_acc = Bank(1000, 0.12, 50, 1234567789)

# bank_acc.deposit(100)
# bank_acc.withdraw(300)

# print(bank_acc.finish_month())

print(bank_acc.balance)
print(bank_acc.bank_account_number)