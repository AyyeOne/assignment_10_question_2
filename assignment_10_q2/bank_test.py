"""
Test the Bank's interaction with multiple account types.
"""

from bank import Bank
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

# complete the main function to test the new Bank class with multiple account types.
def main():
    """
    in the main function, add the following test cases:
    # 1. Add different account types for the same person
    # 2. Test Polymorphic Interest - Only the SavingsAccount should be affected
    # 3. Test Retrieval
    # 4. Show final state
    """
    bank = Bank()

    checking = CheckingAccount("June", "1111", 500.0)
    savings = SavingsAccount("June", "1111", 1000.0)

    print("--- Adding Accounts ---")
    bank.add(checking)
    bank.add(savings)
    print("Keys in bank:", bank.getKeys())
    print()

    print("--- Compute Interest ---")
    totalInterest = bank.computeInterest()
    print("Total interest paid:", totalInterest)
    print()

    print("--- Testing Retrieval ---")
    retrieved = bank.get("June", "1111", "CheckingAccount")
    print("Retrieved Balance:", retrieved.getBalance())
    print()

    print("--- Final Bank State ---")
    print(bank)

if __name__ == "__main__":
    main()