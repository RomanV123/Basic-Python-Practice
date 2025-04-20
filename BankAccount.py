class PersonalInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class BankAccount:
    def __init__(self, personal_info, account_number, initial_balance=0):
        self.personal_info = personal_info
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"
    
    def check_balance(self):
        return f"Account balance: ${self.balance}"
    
    def display_account_info(self):
        return f"{self.personal_info.display_info()}\nAccount Number: {self.account_number}\nBalance: ${self.balance}"


# Main program
accounts = {}  # Dictionary to store accounts

while True:
    ui_menu = input("\nChoose an option:\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit\n")
    
    if ui_menu == "1":
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        account_number = input("Enter account number: ")
        
        try:
            age = int(age)
            initial_balance = float(input("Enter initial deposit amount: "))
            
            # Create personal info and bank account objects
            personal_info = PersonalInfo(name, age)
            account = BankAccount(personal_info, account_number, initial_balance)
            
            # Store account in dictionary
            accounts[account_number] = account
            print(f"Account created successfully!\n{account.display_account_info()}")
            
        except ValueError:
            print("Invalid input. Please enter numeric values for age and balance.")
    
    elif ui_menu == "2":  # Deposit
        account_number = input("Enter your account number: ")
        if account_number in accounts:
            try:
                amount = float(input("Enter deposit amount: "))
                print(accounts[account_number].deposit(amount))
            except ValueError:
                print("Invalid amount.")
        else:
            print("Account not found.")
    
    elif ui_menu == "3":  # Withdraw
        account_number = input("Enter your account number: ")
        if account_number in accounts:
            try:
                amount = float(input("Enter withdrawal amount: "))
                print(accounts[account_number].withdraw(amount))
            except ValueError:
                print("Invalid amount.")
        else:
            print("Account not found.")
    
    elif ui_menu == "4":  # Check Balance
        account_number = input("Enter your account number: ")
        if account_number in accounts:
            print(accounts[account_number].check_balance())
        else:
            print("Account not found.")
    
    elif ui_menu == "5":  # Exit
        print("Thank you for using our banking system. Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.")
