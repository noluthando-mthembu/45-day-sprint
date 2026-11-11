# ====================================================
# Programme: Budget Calculator (Desktop GUI)
# Description: Built using Python's built-in Tkinter library for Windows 11.
# ====================================================

import tkinter as tk 
from tkinter import messagebox

# Create Main App Window
window = tk.Tk()
window.title("Budget Calculator")
window.geometry("350x320")

# Income Input Section
tk.Label(window, text="Monthly Income (R):").pack(pady=5)
income_entry = tk.Entry(window)
income_entry.pack()

# Expense Input Section
tk.Label(window, text="Total Expenses (R):").pack(pady=5)
expense_entry = tk.Entry(window)
expense_entry.pack()

def calculate_budget():
    """Calculates balance from GUI inputs and updates status labels."""
    try:
        income = float(income_entry.get())
        expenses = float(expense_entry.get())
        balance = income - expenses
        
        result_label.config(text=f"Remaining Balance: R{balance:,.2f}")
        
        if balance > 0:
            status_label.config(text="Status: Surplus!", fg="pink")
        elif balance == 0:
            status_label.config(text="Status: Balanced!", fg="white")
        else:
            status_label.config(text="Status: Deficit!", fg="blue")
            
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers only.")

# Calculation Button        
calc_button = tk.Button(window, text="Calculate Balance", command=calculate_budget)
calc_button.pack(pady=15)

# Output Display Section
result_label = tk.Label(window, text="Remaining Balance: R0.00", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

status_label = tk.Label(window, text="Status: Ready", font=("Arial", 10))
status_label.pack(pady=5)

# Run Window Event Loop
window.mainloop()