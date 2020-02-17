from bank import Bank
from bank_account import BankAccount
from customers import Customer
Harold = Customer(1234)
June = Customer(2468)

all_accounts = {"1123456789": BankAccount(0.12, 50, 1000, Harold),
            "1223456789":BankAccount(0.15, 50, 1290, Harold),
            "1233456789":BankAccount(0.12, 50, 1000, June)
            }

my_bank = Bank(all_accounts)
my_bank.withdraw("1223456789", 500, 2468)