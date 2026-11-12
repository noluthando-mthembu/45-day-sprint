# ====================================================
# Programme: Transaction Categoriser (CLI + GUI)
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
    
# GUI
import tkinter as tk 
from tkinter import messagebox

# Window Setup
window = tk.Tk()
window.title("Transaction Categoriser App")
window.geometry("380x350")

def categorise_transaction():
    """Reads input fields, evaluates rules, and displays category on screen."""
    item_text = item_entry.get().strip().lower()
    raw_amount = amount_entry.get().strip()
    
    if not  item_text or not raw_amount:
        messagebox.showerror("Error", "Please fill in both fields.")
        return
    
    try:
        amount = float(raw_amount)
        
        if "milk" in item_text or "bread" in item_text or "supermarket" in item_text:
            category = "Groceries"
            color = "pink"
        elif "bus" in item_text or "train" in item_text or "fuel" in item_text:
            category = "Transport"
            color = "blue"
        elif "electric" in item_text or "water" in item_text or "wifi" in item_text:
            category = "Utilities"
            color = "purple"
        else:
            category = "Other Spending"
            color = "darkorange"
            
        result_label.config(text=f"Item: {item_text.title()}\nAmount: R{amount:,.2f}")
        category_label.config(text=f"Category: {category}", fg=color)
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")

# Input Fields        
tk.Label(window, text="Item Description:").pack(pady=5)
item_entry = tk.Entry(window, width=30)
item_entry.pack()

tk.Label(window, text="Amount (R):").pack(pady=5)
amount_entry = tk.Entry(window, width=30)
amount_entry.pack()

# Categorise Button
btn = tk.Button(window, text="Categorise Transaction", command=categorise_transaction)
btn.pack(pady=15)

# Output Display Labels
result_label = tk.Label(window, text="", font=("Arial Rounded MT", 12))
result_label.pack(pady=5)

category_label = tk.Label(window, text="", font=("Arial Rounded MT", 12, "bold"))
category_label.pack(pady=5)

# Start Window Loop
window.mainloop()