# ====================================================
# Programme: Login Simulator
# Description: Locks account after 3 failed PIN attempts.
# ====================================================

CORRECT_PIN = "0912"
MAX_ATTEMPTS = 3
attempts_used = 0
account_locked = False

while attempts_used < MAX_ATTEMPTS:
    user_pin = input(f"Enter PIN (Attempt {attempts_used + 1}/{MAX_ATTEMPTS}): ").strip()
    
    if user_pin == CORRECT_PIN:
        print("Access Granted! Welcome to your account.")
        break
    else:
        attempts_used +=1
        remaining = MAX_ATTEMPTS - attempts_used
        
        if remaining > 0:
            print("Incorrect PIN. Attempts remaining: {remaining}\n")
        else:
            account_locked = True
            
if account_locked:
    print("\nACCOUNT LOCKED! Maximum failed attempts reached.")
    
# GUI    
import tkinter as tk
from tkinter import messagebox

CORRECT_PIN = "0912"
MAX_ATTEMPTS = 3
attempts_used = 0


def check_pin():
    """Validates PIN entry and locks GUI elements after 3 failed attempts."""
    global attempts_used
    
    entered_pin = pin_entry.get().strip()
    
    if entered_pin == CORRECT_PIN:
        status_label.config(text="ACCESS GRANTED!\nWelcome to your account.", fg="green")
        submit_btn.config(state="disabled")
        pin_entry.config(state="disabled")
    else:
        attempts_used += 1
        remaining = MAX_ATTEMPTS - attempts_used
        
        if remaining > 0:
            status_label.config(text=f"INCORRECT PIN!\nAttempts remaining: {remaining}", fg="red")
            pin_entry.delete(0, tk.END)
        else:
            status_label.config(text="ACCOUNT LOCKED!\nMax failed attempts reached.", fg="darkred")
            submit_btn.config(state="disabled")
            pin_entry.config(state="disabled")
            messagebox.showerror("Security Alert", "ACCOUNT LOCKED!\nToo many incorrect attempts.")


# Window Setup
window = tk.Tk()
window.title("Mock ATM Login Simulator")
window.geometry("350x300")

# Input Masked Text Field
tk.Label(window, text="Enter Security PIN:", font=("Arial", 11)).pack(pady=10)
pin_entry = tk.Entry(window, show="*", font=("Arial", 14), width=15, justify="center")
pin_entry.pack(pady=5)

# Submit Button
submit_btn = tk.Button(window, text="Submit PIN", command=check_pin, font=("Arial", 10, "bold"))
submit_btn.pack(pady=15)

# Dynamic Status Label
status_label = tk.Label(window, text="Attempts Remaining: 3", font=("Arial", 11))
status_label.pack(pady=10)

# Run Window Event Loop
window.mainloop()