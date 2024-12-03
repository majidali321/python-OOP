class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Successfully withdrew ${amount}. Remaining balance: ${self.balance}.")
        else:
            print("Insufficient balance.")

    def deposit(self, amount):
        if amount > 100:
            amount -= 1  # Deduct fee
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")


class Customer:
    def __init__(self, first_name, last_name, gender, age, mobile_number, account):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.mobile_number = mobile_number
        self.account = account


accounts = [
    BankAccount(2002, 500),
    BankAccount(2003, 500),
    BankAccount(2004, 2200)
]

customers = [
    Customer("Majid", "Ali", "Male", 33, 3434200905, accounts[0]),
    Customer("Wajid", "Sadiq", "Male", 32, 3424200906, accounts[1]),
    Customer("Sajid", "Hussain", "Male", 31, 3424200907, accounts[2])
]


def bank_service():
    while True:
        try:
            account_number_input = int(input("Enter your account number: "))
            customer = next((c for c in customers if c.account.account_number == account_number_input), None)

            if customer:
                print(f"\nWelcome {customer.first_name} {customer.last_name}!\n")
                while True:
                    print("Select an operation:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Exit")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        try:
                            amount = float(input("Enter the amount to deposit: "))
                            customer.account.deposit(amount)
                        except ValueError:
                            print("Please enter a valid amount.")
                    elif choice == "2":
                        try:
                            amount = float(input("Enter the amount to withdraw: "))
                            customer.account.withdraw(amount)
                        except ValueError:
                            print("Please enter a valid amount.")
                    elif choice == "3":
                        customer.account.check_balance()
                    elif choice == "4":
                        print("Exiting bank program...")
                        print("Thank you for using our services.")
                        return
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid account number.")
        except ValueError:
            print("Please enter a valid account number.")


# Start the banking service
bank_service()
