from bank import Bank
from bank_account import BankAccount
from customer import Customer
john = Customer(1234)
jane = Customer(2468)

all_ccounts = { "0123456789": BankAccount(0.12, 50, 1000, jane),
            "1123456789":BankAccount(0.15, 50, 1290, john),
            "1223456789":BankAccount(0.12, 50, 1000, jane)
            }

nedbank = Bank(all_ccounts)
nedbank.withdraw("1223456789", 500, 2468)