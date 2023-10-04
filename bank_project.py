""" This is a basic banking system implementation in Python that allows users 
to create accounts, log in, deposit and withdraw funds, check balances, and view mini statements. 
The system consists of two classes: Account and Bankingsystem.
"""

# ---------------BANKING SYSTEM----------------

# the Account class is defined with three instance variables - username, password, and balance. 
# The __init__ method initializes variables with arguments passed while creating an object of this class. 
# The class also contains four methods - deposit, withdraw, get_balance, and mini_statement.

class Account :
    def __init__(self,username,password,balance=0):
        self.username =username
        self.password =password
        self.balance = balance
        self.transactions = []

# The deposit method takes an argument amount and adds it to the balance variable. 
# It then prints a message showing the deposited amount and the updated balance.
   
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited:{amount}")
            print(f"\nAmount deposited: {amount}\nTotal Balance: {self.balance}")
        else:
            print(f"Entered {amount} is invalid")
        
# The withdraw method takes an argument amount and checks if amount is greater than zero and or
#  equal to the amount to be withdrawn. 
# If it is, it deducts the withdrawn amount from the balance and prints a message showing the 
# withdrawn amount and the updated balance. 
# If not, it prints a message saying that there is insufficient balance.

    def withdraw(self,amount):
        if amount>0 and amount <=self.balance:
            self.balance -= amount
            self.transactions.append(f"withdraw:{amount}")
            print(
                f"\nAmount withdrawn: {amount}\nRemaining Balance: {self.balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance
    
    def mini_statement(self):
        print("Mini statement:")
        print(f"Username: {self.username}")
        print(f"transactions: {self.transactions}")
        print(f"Current balance: {self.balance}")


# BankingSystem class is defined. It has one instance variable -accounts -which is a dictionary 
# that stores the username as key and the Account object as value.
   
class Bankingsystem:
    def __init__(self):
        self.accounts ={}

# The create_account method takes two arguments - username and password. 
# It checks if the username already exists in the accounts dictionary. 
# If it does, it prints a message saying that the username already exists. 
# If it does not, it creates a new Account object with the given username and password
# It then prints a message saying that the account was created successfully.

    def create_account(self, username, password):
        if username in self.accounts:
            print("Username already exists")
        else:
            self.accounts[username] = Account(username, password)
            print("\nAccount created successfully")
            print("-------Welcome to ABC Python Bank-------")

# The login method takes two arguments - username and password. 
# It checks if the given username exists in the accounts dictionary. 
# If it does, it retrieves the corresponding Account object and checks if the given password 
# matches the password of that account. 
# If it does, it prints a message saying that the login was successful and returns the Account object. 
# If it does not, it prints a message saying that the password is invalid. If the given username is not 
# found in the accounts dictionary, it prints a message saying that the username is invalid.
    def login(self, username, password):
        if username in self.accounts:
            account = self.accounts[username]
            if account.password == password:
                print("Login Success")
                return account
            else:
                print("Invalid password")
        else:
            print("Invalid username")
        return None

# the main program loop is defined inside the if __name__ == '__main__': block.
# It creates a new BankingSystem object and presents a menu of options to the user - create an account, 
# login, or exit.

if __name__ == '__main__':
    bank = Bankingsystem()

    while True:
        print("\n")
        print("1. Create account")
        print("2. Login")
        print("3. Exit")
        option = input("Enter your option (1-3): ")

# If the user chooses to create an account, the program prompts the user to enter a username and password. 
# It then calls the create_account method of the BankingSystem object with these arguments.

        if option == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            bank.create_account(username, password)

# If the user chooses to login, the program prompts the user to enter their username and password. 
# It then calls the login method of the BankingSystem object with these arguments. 
# If the login is successful, it presents the user with a menu of options - 
# deposit, withdraw, check balance, print mini-statement, or logout.

        elif option == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            account = bank.login(username, password)
            if account is not None:
                while True:
                    print("\n-----Welcome to ABC Python Bank-----")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check balance")
                    print("4. Mini statement")
                    print("5. Logout\n")
                    option = input("Enter your option (1-5): ")

# If user chooses to deposit, the program prompts the user to enter the amount to deposit. 
# It then calls the corresponding method of the Account object.

                    if option == '1':
                        amount = int(input("Enter amount to deposit: "))
                        account.deposit(amount)

# If user chooses to withdraw, the program prompts the user to enter the amount to withdraw. 
# It then calls the corresponding method of the Account object.

                    elif option == '2':
                        amount = int(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                        
# If user chooses to check their balance,the program calls the get_balance method of the Account object and 
# prints the current balance.

                    elif option == '3':
                        print(f"\nCurrent balance: {account.get_balance()}")

# If user chooses to print a mini-statement, the program calls the get_mini_statement method of 
# the Account object and prints the username and current balance.

                    elif option == '4':
                        account.mini_statement()

# If user chooses to logout, break out of the inner WHILE loop and display a message saying 
# "THANK YOU VISIT AGAIN".

                    elif option == '5':
                        print("\n--------THANK YOU VISIT AGAIN--------")
                        break
                    else:
                        print("Invalid option")

# If the user selects option 3, a message is printed indicating that they have exited the program, 
# and break statement is used to exit the outer while loop that displays the main menu.

        elif option == '3':
            print("\n------THANK YOU------")
            break

        else:
            print("Invalid option")


# ----------- FINISHED ------- THANK YOU ---------

