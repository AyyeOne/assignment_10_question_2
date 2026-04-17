"""
File: checkingaccount.py
This module defines the CheckingAccount class.
CheckingAccount does not have interest.
"""

class CheckingAccount:
    """This class represents a checking account with name, PIN, and balance."""

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        """Deposits the given amount and returns None."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """Withdraws the given amount.
        Returns None if successful, or an
        error message if unsuccessful."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def getName(self):
        """Returns the current name."""
        return self.name

    def getPin(self):
        """Returns the current pin."""
        return self.pin

    def __str__(self):
        """Returns the string rep."""
        result = "Type:    Checking\n"
        result += "Name:    " + self.name + "\n"
        result += "PIN:     " + self.pin + "\n"
        result += "Balance: " + str(self.balance)
        return result


def main():
    """Tests the CheckingAccount class to cover the following cases
    1. Test Instantiation
    2. Test String Representation (__str__)
    3. Test Getters
    4. Test Deposit
    5. Test Withdrawals
       Successful withdrawal
       Insufficient funds
       Negative amount
    6. Final State
    """

    print("--- Testing Instantiation ---")
    acct = CheckingAccount("June Zuo", "1234", 500.0)
    print("Account created successfully.")
    print()

    print("--- Testing String Representation ---")
    print(acct)
    print()

    print("--- Testing Getters ---")
    print("Name:   ", acct.getName())
    print("PIN:    ", acct.getPin())
    print("Balance:", acct.getBalance())
    print()

    print("--- Testing Deposit ---")
    acct.deposit(250.0)
    print("Deposited 250.0. New Balance:", acct.getBalance())
    print()

    print("--- Testing Withdrawals ---")
    print("Withdrawing 100.0...")
    result = acct.withdraw(100.0)
    print("Result:", result, "(None means success)")
    print("New Balance:", acct.getBalance())
    print()

    print("Withdrawing 1000.0 (Insufficient funds test)...")
    result = acct.withdraw(1000.0)
    print("Result:", result)
    print()

    print("Withdrawing -50.0 (Negative amount test)...")
    result = acct.withdraw(-50.0)
    print("Result:", result)
    print()

    print("--- Final Account State ---")
    print(acct)


if __name__ == "__main__":
    main()