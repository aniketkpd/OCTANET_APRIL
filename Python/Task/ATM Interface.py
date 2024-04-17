'''
Program for 'ATM Interface' which is a task assigned by Octanet, can perform following operations
    - Transaction History
    - Check Balance
    - Withdraw
    - Deposit
    - Transfer
    - Quit
    
    ============================
    account number : 123456789
    pin : 12345
    ============================
''' 



class ATM:
    def __init__(self, account_number, pin, balance=0, transaction_history=[]):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = transaction_history 

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Withdrawal successful. Current balance:", self.balance)
            self.transaction_history.append(f"Withdrawal: -{amount}") 

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful. Current balance:", self.balance)
        self.transaction_history.append(f"Deposit: +{amount}")

    def check_balance(self):
        print("Current balance:", self.balance)

    def transfer(self, target_account, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Transfer of {amount} to account {target_account} successful.")
            self.transaction_history.append(f"Transfer: -{amount} (to {target_account})")

    def view_transactions(self):
        if not self.transaction_history:
            print("No transactions found.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

def main():
    account_number = 123456789
    pin = 12345
    
    
    
    
    print("Enter login credentials")
    print("========================")
    user_account_number = int(input("Enter your account number : "))
    user_pin = int(input("Enter your pin: "))
    
    if user_account_number == account_number and user_pin == pin:
        print("Login Successfull\n")
    else:
        print("Invalid Credentials")
        exit()

    atm = ATM(account_number, pin)

    while True:
        print("\nWhat would you like to do?")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check balance")
        print("4. Transfer")  # Placeholder for future implementation
        print("5. View transactions")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == 2:
            amount = int(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif choice == 3:
            atm.check_balance()
        elif choice == 4:
            account_num = int(input("Enter reciever's account number : "))
            amountof = int(input("Enter amount to transfer : "))
            atm.transfer(account_num, amountof)
        elif choice == 5:
            atm.view_transactions()
        elif choice == 6:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
