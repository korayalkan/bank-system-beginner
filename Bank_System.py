# Account Class
class Account:
    def __init__(self, account_name, account_number, account_balance=0, account_type="₺"):
        self.account_name = account_name
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_type = account_type
        self.accounts = []



    # Let's see all the accounts
    def show_accounts(self):
        self.accounts.append({"Name": {self.account_name}, "Account Type": {self.account_type}})
        for account in self.accounts:
            print(account)



    # Show account information
    def show_account_information(self):
        print(f'Your Name: {self.account_name},\n'
              f'Your Account Number: {self.account_number},\n'
              f'Your Total Balance: {self.account_type}{self.account_balance},\n'
              f'Your Account Type: {self.account_type}\n')



    # Create a new account
    def create_new_account(self, account_name, account_number, account_balance=0, account_type="₺"):
        new_account = {"Name": {account_name}, "Account Number": {account_number},
                       "Total Balance": {account_balance}, "Account Type": {account_type}}

        # Append the new user to self.accounts
        self.accounts.append(new_account)



    # Delete an existing account
    def delete_account(self, account_number):
        for account in self.accounts:
            if account_number in account:
                del account



    # Deposit
    def account_deposit(self, account_number, amount):

        # If user's account number is right
        if account_number == self.account_number:
            self.account_balance += amount
            print(f'You successfully deposited {self.account_type}{amount} to your account!\n')

        # If user's account number is not right or a different user tries to access
        else:
            print('You can not access to this account!\n')



    # Withdraw
    def account_withdraw(self, account_number, amount):

        # If user's account number is right
        if account_number == self.account_number:
            # If user tries to withdraw more than in his/her account
            if self.account_balance < amount:
                print(f'You can not withdraw that much money,\n'
                      f'Your Current Balance: {self.account_type}{self.account_balance}\n')

            else:
                self.account_balance -= amount
                print(f'You successfully withdrawn {self.account_type}{amount} from your account!\n')

        # If user's account number is not right or a different user tries to access
        else:
            print('You can not access to this account!\n')



    # Transfer money
    def money_transfer(self, other_account, transfer_amount):
        if self.account_balance < transfer_amount:
            print(f'You can not transfer that much money,\n'
                  f'Your Current Balance: {self.account_type}{self.account_balance}.\n')

        else:
            self.account_balance -= transfer_amount
            other_account.account_balance += transfer_amount
            print(f'You successfully transferred {self.account_type}{transfer_amount} to "Account {other_account}" !\n')



# Created users
user1 = Account("Koray", 1020, 1000, "€")
user2 = Account("Alkan", 6320, 1000, "$")

# Transfer
user1.money_transfer(user2, 100)

# Show the account information
user1.show_account_information()
user2.show_account_information()
