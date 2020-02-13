from bank_account import BankAccount
class Bank(BankAccount):

    def __init__(self, bank_accounts=[] ):
        self.bank_accounts = bank_accounts

    def register_account(self, account_object):
        self.bank_accounts.append(account_object)
        print("Account with account number: " + account_object.bank_account_number + " created successfully!")

    def withdraw(self, bank_account_number, amount):
        if len(bank_account_number) == 10:
            for bank_acc in self.bank_accounts:
                if bank_acc.bank_account_number == bank_account_number:
                    bank_acc.withdraw(amount)
                    return "Account Balance of " + bank_acc.bank_account_number + ": R" + str(bank_acc.balance)
        raise Exception ('ERROR: Invalid Account Number ')        

    def deposit(self, bank_account_number, amount):
        '''
        First check if the bank account number exists in the accounts list
        and deposit iff it exist.
        '''
        if len(bank_account_number) == 10:
            for bank_acc in self.bank_accounts:
                if bank_acc.bank_account_number == bank_account_number:
                    bank_acc.deposit(amount)
                    return "Account Balance of " + bank_acc.bank_account_number + ": R" + str(bank_acc.balance)
        raise Exception ('ERROR: Invalid Account Number ') 
            

    def transfer(self, from_bank_account_number, to_bank_account_number, amount):
        # These will be used later to check if both accounts exist
        from_account_exist = False
        to_account_exist = False
        # These will store objects that match passed account numbers
        from_account_object = None
        to_account_object = None
        # check if both accounts are valid (exists in my list of bank accounts)
        for bank_acc in self.bank_accounts:
            if bank_acc.bank_account_number == from_bank_account_number:
                from_account_exist = True
                from_account_object = bank_acc
                break
        
        for bank_acc in self.bank_accounts:
            if bank_acc.bank_account_number == to_bank_account_number:
                to_account_exist = True
                to_account_object = bank_acc
                break  
        if from_account_exist == True and to_account_exist == True:
            from_account_object.withdraw(amount)
            print( "Account Balance of " + from_account_object.bank_account_number + ": R" + str(from_account_object.balance))
            to_account_object.deposit(amount)
            print( "Account Balance of " + to_account_object.bank_account_number + ": R" + str(to_account_object.balance))

bank = Bank()
bank_acc1 = BankAccount("1234567789",1000, 0.12, 50)
print("Current bank accounts before registration")
print(bank.bank_accounts)
bank.register_account(bank_acc1)
print("Current bank accounts after registration")
print(bank.bank_accounts)
print(type(bank_acc1))

# print(bank.withdraw("1234567789", 300))
# print(bank.deposit("1234567789", 100))
# print("After transfer")
# print(bank.transfer(1234567769, 9877654321, 200))