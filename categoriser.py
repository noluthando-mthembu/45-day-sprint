# ====================================================
# Programme: Transaction Categoriser
# Description: Evaluates text keywords and assigns spending categories.
# ====================================================

item_name = input("Enter item description: ").strip().lower()
raw_amount = input("Enter transaction amount (R): ").strip()

try:
    amount = float(raw_amount)
    
    if "milk" in item_name or "bread" in item_name or "supermarket" in item_name:
        category = "Groceries"
    elif "bus" in item_name or "train" in item_name or "fuel" in item_name:
        category = "Transport"
    elif "electric" in item_name or "water" in item_name or "wifi" in item_name:
        category = "Utilities"
    else:
        category = "Other Spending"
        
    print(f"\nItem: {item_name.title()}")
    print(f"Amount: R{amount:,.2f}")
    print(f"Assigned Category: {category}")
    
except ValueError:
    print("Error: Invalid numeric amount entered.")