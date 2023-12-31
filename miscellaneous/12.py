class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store user account information

    def create_account(self, account_number, name, balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = {'name': name, 'balance': balance}
            return "Account created successfully."
        else:
            return "Account already exists. Choose a different account number."

    def get_balance(self, account_number):
        if account_number in self.accounts:
            return f"Account balance for {self.accounts[account_number]['name']}: ${self.accounts[account_number]['balance']:.2f}"
        else:
            return "Account not found."

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            return f"Deposited ${amount:.2f} to {self.accounts[account_number]['name']}'s account. New balance: ${self.accounts[account_number]['balance']:.2f}"
        else:
            return "Account not found."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]['balance']:
                self.accounts[account_number]['balance'] -= amount
                return f"Withdrew ${amount:.2f} from {self.accounts[account_number]['name']}'s account. New balance: ${self.accounts[account_number]['balance']:.2f}"
            else:
                return "Insufficient funds."
        else:
            return "Account not found."

def main():
    bank = Bank()

    while True:
        print("Banking System Menu:")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: $"))
            result = bank.create_account(account_number, name, initial_balance)
            print(result)
        elif choice == "2":
            account_number = input("Enter account number: ")
            result = bank.get_balance(account_number)
            print(result)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: $"))
            result = bank.deposit(account_number, amount)
            print(result)
        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: $"))
            result = bank.withdraw(account_number, amount)
            print(result)
        elif choice == "5":
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
