class Bank:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, bank_account_number, amount):
        bank_account_number = str(bank_account_number)
        if len(bank_account_number) != 10:
            error_msg = 'ERROR: Invalid Account Number '
            raise Exception (error_msg)

        elif len(bank_account_number) == 10:
                self.balance -= amount
                return "Account Balance of " + bank_account_number + ": R" + str(self.balance)         

    def deposit(self, bank_account_number, amount):
        bank_account_number = str(bank_account_number)
        if len(bank_account_number) != 10:
            error_msg = 'ERROR: Invalid Account Number '
            raise Exception (error_msg)
        
        elif len(bank_account_number) == 10:
                self.balance += amount
                return "Account Balance of " + bank_account_number + ": R" + str(self.balance)

    # def transfer(self, from_bank_account_number, to_bank_account_number, amount):
    #      from_bank_account_number = str(from_bank_account_number)
    #      to_bank_account_number = str(to_bank_account_number)
    #     if len(from_bank_account_number) != 10 and len(to_bank_account_number) != 10:
    #         error_msg = 'ERROR: Invalid Account Number '
    #         raise Exception (error_msg)
    #     else:
    #         if len(from_bank_account_number) == 10 and len(to_bank_account_number) == 10:
                

bank = Bank(1000)

print(bank.withdraw(1234567789, 300))
print(bank.deposit(1234567789, 100))
# print(bank.transfer(1234567769, 9877654321, 200))