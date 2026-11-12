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