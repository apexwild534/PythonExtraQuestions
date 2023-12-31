class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive number."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew {amount}. New balance: {self.balance}"
            else:
                return "Insufficient funds."
        else:
            return "Invalid withdrawal amount. Please enter a positive number."

def main():
    atm = ATM(1000)  # Initialize with a balance of 1000

    while True:
        print("ATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            balance = atm.check_balance()
            print(f"Your balance is: {balance}")
        elif choice == "2":
            amount = float(input("Enter the deposit amount: "))
            result = atm.deposit(amount)
            print(result)
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            result = atm.withdraw(amount)
            print(result)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
