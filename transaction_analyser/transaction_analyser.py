# ====================================================
# Programme: Interactive Transaction Summary App (Dual CLI + GUI Interface)
# Description: Demonstrates dynamic input, loops, lists, dicts, sets, and custom pop-ups.
# ====================================================

import tkinter as tk

# Styling Constants
DARK_BACKGROUND = "#241b2f"
PANEL_BACKGROUND = "#2f2142"
NEON_PINK = "#ff7edb"
NEON_CYAN = "#36f9f6"
NEON_YELLOW = "#fefe60"
TEXT_COLOR = "#f8f8f2"
MAIN_FONT = ("Arial Rounded MT Bold", 10)
BOLD_FONT = ("Arial Rounded MT Bold", 11, "bold")
TITLE_FONT = ("Arial Rounded MT Bold", 14, "bold")

# Dynamic Transaction List Storage
transaction_list = []


def process_analysis(data_list):
    """Core calculation engine shared by both CLI and GUI interfaces."""
    if not data_list:
        return None

    total_value = 0.0
    maximum_value = data_list[0]["amount"]
    minimum_value = data_list[0]["amount"]
    category_counts = {}
    unique_categories = set()

    for item in data_list:
        amount = item["amount"]
        category = item["category"]
        
        total_value += amount
        
        if amount > maximum_value:
            maximum_value = amount
        if amount < minimum_value:
            minimum_value = amount
            
        category_counts[category] = category_counts.get(category, 0) + 1
        unique_categories.add(category)

    average_value = total_value / len(data_list)
    
    return {
        "total": total_value,
        "average": average_value,
        "maximum": maximum_value,
        "minimum": minimum_value,
        "counts": category_counts,
        "unique": sorted(unique_categories),
        "total_count": len(data_list)
    }


def run_cli_mode():
    """Interactive Terminal Command-Line Interface."""
    global transaction_list
    print("\n====================================")
    print("   TRANSACTION ANALYSER (CLI MODE)  ")
    print("====================================")
    
    while True:
        print("\n1. Add a New Transaction")
        print("2. Analyse Entered Transactions")
        print("3. Load Default Mock Dataset")
        print("4. Clear All Transactions")
        print("5. Exit CLI Mode")
        
        user_choice = input("\nEnter choice (1-5): ").strip()
        
        if user_choice == "1":
            customer_name = input("Enter Customer Name: ").strip()
            category = input("Enter Category (Groceries/Transport/etc.): ").strip().capitalize()
            raw_amount = input("Enter Amount (R): ").strip()
            try:
                amount = float(raw_amount)
                if amount <= 0:
                    print("Error: Amount must be greater than R0.00.")
                    continue
                transaction_list.append({
                    "customer": customer_name,
                    "category": category,
                    "amount": amount
                })
                print(f"Success! Added R{amount:,.2f} for {customer_name} under '{category}'.")
            except ValueError:
                print("Error: Invalid numeric amount.")
                
        elif user_choice == "2":
            result = process_analysis(transaction_list)
            if result is None:
                print("\n[ALERT] No transactions found! Add a transaction first (Option 1).")
            else:
                print("\n--- ANALYSIS RESULTS ---")
                print(f"Total Transactions: {result['total_count']}")
                print(f"Total Spend:        R{result['total']:,.2f}")
                print(f"Average Spend:      R{result['average']:,.2f}")
                print(f"Maximum Spend:      R{result['maximum']:,.2f}")
                print(f"Minimum Spend:      R{result['minimum']:,.2f}")
                print("\nCategory Counts (Dictionary):")
                for category_name, category_count in result["counts"].items():
                    print(f"  • {category_name}: {category_count}")
                print(f"\nUnique Categories (Set): {', '.join(result['unique'])}")
                
        elif user_choice == "3":
            transaction_list = [
                {"customer": "Alice", "category": "Groceries", "amount": 45.50},
                {"customer": "Bob", "category": "Transport", "amount": 15.00},
                {"customer": "Charlie", "category": "Groceries", "amount": 80.25},
                {"customer": "Diana", "category": "Utilities", "amount": 120.00}
            ]
            print("Loaded 4 default mock transactions into list!")
            
        elif user_choice == "4":
            transaction_list.clear()
            print("All transactions cleared from list.")
            
        elif user_choice == "5":
            print("Exiting CLI Mode. Goodbye!")
            break
        else:
            print("Invalid choice! Enter a number from 1 to 5.")
            continue


def show_popup_dialog(title_text, message_text):
    """Custom Toplevel Pop-up Modal Window."""
    popup_window = tk.Toplevel(window)
    popup_window.title(title_text)
    popup_window.geometry("360x200")
    popup_window.configure(bg=DARK_BACKGROUND)
    
    tk.Label(popup_window, text=title_text, font=TITLE_FONT, fg=NEON_PINK, bg=DARK_BACKGROUND).pack(pady=10)
    tk.Label(popup_window, text=message_text, font=MAIN_FONT, fg=NEON_CYAN, bg=DARK_BACKGROUND, wraplength=320).pack(pady=10)
    
    ok_button = tk.Button(
        popup_window, 
        text="OK", 
        font=BOLD_FONT, 
        fg=DARK_BACKGROUND, 
        bg=NEON_CYAN, 
        activebackground=NEON_PINK, 
        activeforeground=DARK_BACKGROUND,
        command=popup_window.destroy
    )
    ok_button.pack(pady=10)


def add_gui_transaction():
    """Collects input from text boxes, validates, and adds to storage list."""
    customer_name = customer_entry.get().strip()
    category = category_entry.get().strip().capitalize()
    raw_amount = amount_entry.get().strip()
    
    if not customer_name or not category or not raw_amount:
        show_popup_dialog("Input Error", "Please fill in all 3 input fields before adding!")
        return
        
    try:
        amount = float(raw_amount)
        if amount <= 0:
            show_popup_dialog("Input Error", "Amount must be greater than R0.00!")
            return
            
        transaction_list.append({
            "customer": customer_name, 
            "category": category, 
            "amount": amount
        })
        show_popup_dialog("Success", f"Added R{amount:,.2f} for {customer_name} under '{category}'!")
        
        customer_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        update_gui_display()
        
    except ValueError:
        show_popup_dialog("Input Error", "Please enter a valid numeric amount.")


def update_gui_display():
    """Updates desktop GUI elements with dynamic calculation results."""
    result = process_analysis(transaction_list)
    
    if result is None:
        stats_label.config(text="No transactions in memory. Enter data above!")
        counts_label.config(text="")
        unique_label.config(text="")
        return

    summary_text = (
        f"Total Entries: {result['total_count']} | Total Spend: R{result['total']:,.2f}\n"
        f"Average Spend: R{result['average']:,.2f}\n"
        f"Max Spend: R{result['maximum']:,.2f} | Min Spend: R{result['minimum']:,.2f}"
    )
    stats_label.config(text=summary_text)

    counts_text = "Category Counts (Dict):\n"
    for category_name, category_count in result["counts"].items():
        counts_text += f"• {category_name}: {category_count}  "
    counts_label.config(text=counts_text)

    unique_text = f"Unique Categories (Set): {', '.join(result['unique'])}"
    unique_label.config(text=unique_text)


def load_mock_gui():
    """Populates list with mock data."""
    global transaction_list
    transaction_list = [
        {"customer": "Alice", "category": "Groceries", "amount": 45.50},
        {"customer": "Bob", "category": "Transport", "amount": 15.00},
        {"customer": "Charlie", "category": "Groceries", "amount": 80.25},
        {"customer": "Diana", "category": "Utilities", "amount": 120.00}
    ]
    show_popup_dialog("Data Loaded", "Loaded 4 mock transactions into list!")
    update_gui_display()


def clear_all_gui():
    """Clears stored transaction list."""
    global transaction_list
    transaction_list.clear()
    update_gui_display()
    show_popup_dialog("Cleared", "All transactions cleared from list.")


def launch_gui_mode():
    """Desktop Graphical User Interface App."""
    global window, customer_entry, category_entry, amount_entry, stats_label, counts_label, unique_label
    
    # 1. Window Setup
    window = tk.Tk()
    window.title("Transaction Analyser App")
    window.geometry("480x640")
    window.configure(bg=DARK_BACKGROUND)

    # 2. Input Data Section
    title_label = tk.Label(window, text="TRANSACTION ANALYSER", font=TITLE_FONT, fg=NEON_PINK, bg=DARK_BACKGROUND)
    title_label.pack(pady=10)

    input_frame = tk.Frame(window, bg=PANEL_BACKGROUND, bd=1, relief="solid")
    input_frame.pack(pady=5, padx=15, fill="x")

    tk.Label(input_frame, text="Customer Name:", font=MAIN_FONT, fg=TEXT_COLOR, bg=PANEL_BACKGROUND).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    customer_entry = tk.Entry(input_frame, font=MAIN_FONT, width=20)
    customer_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Category:", font=MAIN_FONT, fg=TEXT_COLOR, bg=PANEL_BACKGROUND).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    category_entry = tk.Entry(input_frame, font=MAIN_FONT, width=20)
    category_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Amount (R):", font=MAIN_FONT, fg=TEXT_COLOR, bg=PANEL_BACKGROUND).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    amount_entry = tk.Entry(input_frame, font=MAIN_FONT, width=20)
    amount_entry.grid(row=2, column=1, padx=5, pady=5)

    add_button = tk.Button(
        input_frame, 
        text="Add Transaction", 
        font=BOLD_FONT, 
        fg=DARK_BACKGROUND, 
        bg=NEON_CYAN, 
        activebackground=NEON_PINK, 
        activeforeground=DARK_BACKGROUND,
        command=add_gui_transaction
    )
    add_button.grid(row=3, column=0, columnspan=2, pady=10)

    # 3. Calculation Button
    button_frame = tk.Frame(window, bg=DARK_BACKGROUND)
    button_frame.pack(pady=10)

    calculate_button = tk.Button(
        button_frame, 
        text="Analyse Transactions", 
        font=BOLD_FONT, 
        fg=DARK_BACKGROUND, 
        bg=NEON_CYAN, 
        activebackground=NEON_PINK, 
        activeforeground=DARK_BACKGROUND,
        command=update_gui_display
    )
    calculate_button.pack(side="left", padx=5)

    mock_button = tk.Button(
        button_frame, 
        text="Load Mock Data", 
        font=BOLD_FONT, 
        fg=DARK_BACKGROUND, 
        bg=NEON_YELLOW, 
        activebackground=NEON_PINK, 
        activeforeground=DARK_BACKGROUND,
        command=load_mock_gui
    )
    mock_button.pack(side="left", padx=5)

    clear_button = tk.Button(
        button_frame, 
        text="Clear All", 
        font=BOLD_FONT, 
        fg=TEXT_COLOR, 
        bg="#ff5555", 
        activebackground=NEON_PINK, 
        activeforeground=DARK_BACKGROUND,
        command=clear_all_gui
    )
    clear_button.pack(side="left", padx=5)

    # 4. Output Display Section
    display_frame = tk.Frame(window, bg=PANEL_BACKGROUND, bd=2, relief="solid")
    display_frame.pack(pady=10, padx=15, fill="both", expand=True)

    stats_label = tk.Label(display_frame, text="No transactions added yet.", font=MAIN_FONT, fg=TEXT_COLOR, bg=PANEL_BACKGROUND, justify="left")
    stats_label.pack(anchor="w", padx=15, pady=10)

    counts_label = tk.Label(display_frame, text="", font=MAIN_FONT, fg=NEON_CYAN, bg=PANEL_BACKGROUND, justify="left")
    counts_label.pack(anchor="w", padx=15, pady=5)

    unique_label = tk.Label(display_frame, text="", font=BOLD_FONT, fg=NEON_PINK, bg=PANEL_BACKGROUND, justify="left", wraplength=400)
    unique_label.pack(anchor="w", padx=15, pady=10)

    # 5. Execution Trigger
    window.mainloop()


if __name__ == "__main__":
    print("====================================")
    print("   SELECT APPLICATION INTERFACE     ")
    print("====================================")
    print("1. Run Terminal CLI Mode")
    print("2. Launch Interactive Desktop GUI App")
    
    app_choice = input("\nEnter choice (1 or 2): ").strip()
    
    if app_choice == "1":
        run_cli_mode()
    elif app_choice == "2":
        launch_gui_mode()
    else:
        print("Invalid entry. Defaulting to CLI Mode...")
        run_cli_mode()