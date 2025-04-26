import time

class BankAccount:
    accounts = {}
    transactions = {}

    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.accounts[account_number] = self
        BankAccount.transactions[account_number] = []

    def log_transaction(self, transaction_type, amount):
        BankAccount.transactions[self.account_number].append(
            (transaction_type, amount, self.balance))

    def deposit(self, amount):
        if amount >= 500:
            self.balance += amount
            self.log_transaction("Deposit", amount)
        else:
            print("Minimum deposit is ₹500!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.log_transaction("Withdrawal", amount)
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Balance: ₹{self.balance}")

    def show_transaction_history(self):
        transactions = BankAccount.transactions.get(self.account_number, [])
        if transactions:
            for trans_type, amount, balance in transactions:
                print(f"{trans_type}: ₹{amount} | Balance After: ₹{balance}")
        else:
            print("No transactions found.")

class SavingsAccount(BankAccount):
    MIN_BALANCE = 1000

    def __init__(self, account_number, account_holder, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        if balance < self.MIN_BALANCE:
            print(f"Warning: Minimum balance for savings is ₹{self.MIN_BALANCE}")

class CurrentAccount(BankAccount):
    MIN_BALANCE = 5000

    def __init__(self, account_number, account_holder, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        if balance < self.MIN_BALANCE:
            print(f"Warning: Minimum balance for current is ₹{self.MIN_BALANCE}")

def find_account(account_number):
    return BankAccount.accounts.get(account_number)

def main():
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. View Transactions\n6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            acc_number = int(input("Enter account number: "))
            name = input("Enter account holder's name: ")
            acc_type = input("Enter account type (savings/current): ").strip().lower()
            initial_deposit = float(input("Enter initial deposit: "))
            if acc_type == "savings":
                SavingsAccount(acc_number, name, initial_deposit)
            elif acc_type == "current":
                CurrentAccount(acc_number, name, initial_deposit)
            else:
                print("Invalid account type!")

        elif choice in "2345":
            acc_number = int(input("Enter account number: "))
            account = find_account(acc_number)
            if account:
                if choice == "2":
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif choice == "3":
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                elif choice == "4":
                    account.check_balance()
                elif choice == "5":
                    account.show_transaction_history()
            else:
                print("Account not found!")

        elif choice == "6":
            print("Thanks for banking with us! 🏦✨")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
