# ====================================================
# Programme: Personal Budget Calculator
# Description: Accepts income and expenses, validates numeric
#              entries, calculates remaining balance, and outputs summary.
# ====================================================

def get_valid_amount(prompt):
    """
    Prompts the user for a number and validates the input.
    Loops until the user enters a valid, non-negative number.
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Error: Input cannot be blank. Please enter a number.")
            continue
        try:
            amount = float(user_input)
            if amount < 0:
                print("Error: Amount cannot be negative. Please enter 0 or higher.")
                continue
            return amount
        except ValueError:
            print("Error: Invalid entry. Please enter numbers only (e.g. 1209.12).")
            
def main():
    print("=======================")
    print("   BUDGET CALCULATOR   ")
    print("=======================\n")
    
    #1. Collect Income
    salary = get_valid_amount("Enter monthly salary (R): ")
    other_income = get_valid_amount("Enter additional income (R): ")
    total_income = salary + other_income
    
    print("\n---------------------")
    #2. Collect Expenses
    rent = get_valid_amount("Enter rent / mortgage (R): ")
    bills = get_valid_amount("Enter utilities / bills (R): ")
    groceries = get_valid_amount("Enter groceries expense (R): ")
    
    total_expenses = rent + bills + groceries
    #3. Calculate Balance
    remaining_balance = total_income - total_expenses
    
    #4. Output Summary
    print("\n====================")
    print("    BUDGET SUMMARY    ")
    print("======================")
    print(f"Total Income:       R{total_income:,.2f}")
    print(f"Total Expense:      R{total_expenses:,.2f}")
    print(f"Remaining Balance:      R{remaining_balance:,.2f}")
    print("----------------------")
    
    if remaining_balance > 0:
        print("Status: Surplus! You are within your budget.")
    elif remaining_balance == 0:
        print("Status: Balanced! You broke even exactly.")
    else:
        print("Status: Deficit! You are over budget.")
        
if __name__ == "__main__":
    main()