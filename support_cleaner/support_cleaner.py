# ====================================================
# Programme: Support Request Data Cleaner App (Dual CLI + GUI Interface)
# Description: Demonstrates open(), with statements, csv.DictReader, DictWriter, and try/except traceback handling.
# ====================================================

import csv
import os
import tkinter as tk

# Styling Constants
DARK_BACKGROUND = "#1e1e2e"
PANEL_BACKGROUND = "#2b2b3d"
PRIMARY_ACCENT_COLOR = "#89b4fa"
SECONDARY_ACCENT_COLOR = "#a6e3a1"
WARNING_ACCENT_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
MAIN_FONT = ("Arial Rounded MT Bold", 10)
BOLD_FONT = ("Arial Rounded MT Bold", 11, "bold")
TITLE_FONT = ("Arial Rounded MT Bold", 14, "bold")

# Dynamic Support Request List Storage
support_request_list = []


def create_sample_csv_file(file_path):
    """Generates a sample CSV dataset with valid rows, duplicates, and missing values."""
    sample_data = [
        {"ticket_identifier": "TCK-101", "customer_name": "Alice Smith", "issue_description": "Login authentication failure", "priority_level": "High"},
        {"ticket_identifier": "TCK-102", "customer_name": "Bob Jones", "issue_description": "Payment gateway timeout", "priority_level": "Medium"},
        {"ticket_identifier": "TCK-101", "customer_name": "Alice Smith", "issue_description": "Duplicate ticket entry", "priority_level": "High"},
        {"ticket_identifier": "TCK-103", "customer_name": "", "issue_description": "Missing customer name", "priority_level": "Low"},
        {"ticket_identifier": "TCK-104", "customer_name": "Charlie Brown", "issue_description": "", "priority_level": "Medium"},
        {"ticket_identifier": "TCK-105", "customer_name": "Diana Prince", "issue_description": "Password reset link expired", "priority_level": "Low"}
    ]
    
    with open(file_path, "w", newline="", encoding="utf-8") as file_handle:
        field_names = ["ticket_identifier", "customer_name", "issue_description", "priority_level"]
        writer = csv.DictWriter(file_handle, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(sample_data)


def process_support_requests(input_file_path, clean_output_file_path, error_report_file_path):
    """Reads raw CSV, filters out duplicate IDs and missing values, and writes output files."""
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found at: {input_file_path}")

    clean_tickets = []
    error_tickets = []
    seen_ticket_identifiers = set()

    with open(input_file_path, "r", newline="", encoding="utf-8") as file_handle:
        reader = csv.DictReader(file_handle)
        
        if reader.fieldnames is None:
            raise ValueError("The provided file is empty or missing headers.")

        for row_number, row in enumerate(reader, start=2):
            ticket_identifier = row.get("ticket_identifier", "").strip()
            customer_name = row.get("customer_name", "").strip()
            issue_description = row.get("issue_description", "").strip()
            priority_level = row.get("priority_level", "").strip()

            if not ticket_identifier or not customer_name or not issue_description or not priority_level:
                error_tickets.append({
                    "ticket_identifier": ticket_identifier,
                    "customer_name": customer_name,
                    "issue_description": issue_description,
                    "priority_level": priority_level,
                    "error_reason": f"Malformed row / Missing value on line {row_number}"
                })
                continue

            if ticket_identifier in seen_ticket_identifiers:
                error_tickets.append({
                    "ticket_identifier": ticket_identifier,
                    "customer_name": customer_name,
                    "issue_description": issue_description,
                    "priority_level": priority_level,
                    "error_reason": f"Duplicate ticket identifier '{ticket_identifier}' on line {row_number}"
                })
                continue

            seen_ticket_identifiers.add(ticket_identifier)
            clean_tickets.append({
                "ticket_identifier": ticket_identifier,
                "customer_name": customer_name,
                "issue_description": issue_description,
                "priority_level": priority_level
            })

    field_names = ["ticket_identifier", "customer_name", "issue_description", "priority_level"]
    with open(clean_output_file_path, "w", newline="", encoding="utf-8") as clean_file_handle:
        clean_writer = csv.DictWriter(clean_file_handle, fieldnames=field_names)
        clean_writer.writeheader()
        clean_writer.writerows(clean_tickets)

    error_field_names = ["ticket_identifier", "customer_name", "issue_description", "priority_level", "error_reason"]
    with open(error_report_file_path, "w", newline="", encoding="utf-8") as error_file_handle:
        error_writer = csv.DictWriter(error_file_handle, fieldnames=error_field_names)
        error_writer.writeheader()
        error_writer.writerows(error_tickets)

    return {
        "total_processed": len(clean_tickets) + len(error_tickets),
        "clean_count": len(clean_tickets),
        "error_count": len(error_tickets),
        "clean_tickets": clean_tickets,
        "error_tickets": error_tickets
    }


def run_cli_mode():
    """Interactive Terminal Command-Line Interface."""
    sample_file = "support_requests.csv"
    clean_file = "clean_support_requests.csv"
    error_file = "error_report.csv"

    print("\n====================================")
    print("  SUPPORT REQUEST CLEANER (CLI MODE)")
    print("====================================")

    while True:
        print("\n1. Create Sample CSV Data File")
        print("2. Run Data Cleaning & Error Inspection")
        print("3. Test Edge Case: Missing File")
        print("4. Test Edge Case: Empty File")
        print("5. Exit CLI Mode")

        user_choice = input("\nEnter choice (1-5): ").strip()

        if user_choice == "1":
            create_sample_csv_file(sample_file)
            print(f"Success! Created sample file at '{sample_file}'.")

        elif user_choice == "2":
            try:
                if not os.path.exists(sample_file):
                    create_sample_csv_file(sample_file)

                result = process_support_requests(sample_file, clean_file, error_file)
                print("\n--- CLEANING RESULTS SUMMARY ---")
                print(f"Total Rows Processed: {result['total_processed']}")
                print(f"Clean Records Saved:  {result['clean_count']} -> {clean_file}")
                print(f"Defective Rows Flagged: {result['error_count']} -> {error_file}")

                print("\nFlagged Error Details:")
                for ticket in result["error_tickets"]:
                    print(f"  • ID: {ticket['ticket_identifier']} | Reason: {ticket['error_reason']}")

            except Exception as exception_instance:
                print(f"\n[TRACEBACK / ERROR ENCOUNTERED]\nType: {type(exception_instance).__name__}\nDetail: {exception_instance}")

        elif user_choice == "3":
            try:
                process_support_requests("non_existent_requests.csv", clean_file, error_file)
            except FileNotFoundError as exception_instance:
                print("\n[TRACEBACK HANDLED - READ FROM BOTTOM UPWARDS]")
                print(f"Error Type: {type(exception_instance).__name__}")
                print(f"Error Message: {exception_instance}")

        elif user_choice == "4":
            empty_file_path = "empty_requests.csv"
            with open(empty_file_path, "w", encoding="utf-8") as empty_handle:
                pass
            try:
                process_support_requests(empty_file_path, clean_file, error_file)
            except Exception as exception_instance:
                print("\n[TRACEBACK HANDLED - READ FROM BOTTOM UPWARDS]")
                print(f"Error Type: {type(exception_instance).__name__}")
                print(f"Error Message: {exception_instance}")

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
    popup_window.geometry("380x220")
    popup_window.configure(bg=DARK_BACKGROUND)

    tk.Label(popup_window, text=title_text, font=TITLE_FONT, fg=WARNING_ACCENT_COLOR, bg=DARK_BACKGROUND).pack(pady=10)
    tk.Label(popup_window, text=message_text, font=MAIN_FONT, fg=TEXT_COLOR, bg=DARK_BACKGROUND, wraplength=340, justify="center").pack(pady=10)

    ok_button = tk.Button(
        popup_window,
        text="OK",
        font=BOLD_FONT,
        fg=DARK_BACKGROUND,
        bg=PRIMARY_ACCENT_COLOR,
        activebackground=SECONDARY_ACCENT_COLOR,
        activeforeground=DARK_BACKGROUND,
        command=popup_window.destroy
    )
    ok_button.pack(pady=10)


def add_gui_support_request():
    """Collects input from text boxes, appends to CSV file, and re-cleans data."""
    ticket_identifier = ticket_entry.get().strip()
    customer_name = customer_entry.get().strip()
    issue_description = issue_entry.get().strip()
    priority_level = priority_entry.get().strip().capitalize()

    if not ticket_identifier or not customer_name or not issue_description or not priority_level:
        show_popup_dialog("Input Error", "Please fill in all 4 input fields before adding!")
        return

    sample_file = "support_requests.csv"
    file_exists = os.path.exists(sample_file)

    with open(sample_file, "a", newline="", encoding="utf-8") as file_handle:
        field_names = ["ticket_identifier", "customer_name", "issue_description", "priority_level"]
        writer = csv.DictWriter(file_handle, fieldnames=field_names)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "ticket_identifier": ticket_identifier,
            "customer_name": customer_name,
            "issue_description": issue_description,
            "priority_level": priority_level
        })

    show_popup_dialog("Ticket Added", f"Added '{ticket_identifier}' for {customer_name} to '{sample_file}'!")
    ticket_entry.delete(0, tk.END)
    customer_entry.delete(0, tk.END)
    issue_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)
    run_gui_cleaning_process()


def run_gui_cleaning_process():
    """Updates desktop GUI elements with cleaning metrics."""
    sample_file = "support_requests.csv"
    clean_file = "clean_support_requests.csv"
    error_file = "error_report.csv"

    if not os.path.exists(sample_file):
        create_sample_csv_file(sample_file)

    try:
        result = process_support_requests(sample_file, clean_file, error_file)
        summary_text = (
            f"Total Processed: {result['total_processed']} Rows\n"
            f"Clean Records Saved: {result['clean_count']} -> {clean_file}\n"
            f"Flagged Defects: {result['error_count']} -> {error_file}"
        )
        stats_label.config(text=summary_text)

        error_details = "Flagged Error Log:\n"
        for ticket in result["error_tickets"]:
            error_details += f"• ID: {ticket['ticket_identifier']} | {ticket['error_reason']}\n"
        
        if not result["error_tickets"]:
            error_details += "• No errors found! All records are clean."

        error_label.config(text=error_details)

    except Exception as exception_instance:
        show_popup_dialog("Cleaning Exception", f"Traceback Error: {exception_instance}")


def test_missing_file_gui():
    """Tests missing file exception and demonstrates traceback handling."""
    try:
        process_support_requests("non_existent_file.csv", "clean.csv", "error.csv")
    except FileNotFoundError as exception_instance:
        show_popup_dialog("FileNotFoundError Handled", f"Traceback read from bottom upwards:\n{exception_instance}")


def launch_gui_mode():
    """Desktop Graphical User Interface App."""
    global window, ticket_entry, customer_entry, issue_entry, priority_entry, stats_label, error_label

    # 1. Window Setup
    window = tk.Tk()
    window.title("Support Request Data Cleaner App")
    window.geometry("500x680")
    window.configure(bg=DARK_BACKGROUND)

    # 2. Input Data Section
    title_label = tk.Label(window, text="SUPPORT REQUEST CLEANER", font=TITLE_FONT, fg=PRIMARY_ACCENT_COLOR, bg=DARK_BACKGROUND)
    title_label.pack(pady=10)

    input_frame = tk.Frame(window, bg=PANEL_BACKGROUND, bd=1, relief="solid")
    input_frame.pack(pady=5, padx=15, fill="x")

    tk.Label(input_frame, text="Ticket ID:", font=MAIN_FONT, fg=TEXT_COLOR, bg=PANEL_BACKGROUND).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ticket_entry = tk.Entry(input_frame, font=MAIN_FONT, width=22)
    ticket_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Customer Name:", font=MAIN_FONT, fg=TEXT_COLOR, bg=PANEL_BACKGROUND).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    customer_entry = tk.Entry(input_frame, font=MAIN_FONT, width=22)
    customer_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Issue Description:", font=MAIN_FONT, fg=TEXT_COLOR, bg=PANEL_BACKGROUND).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    issue_entry = tk.Entry(input_frame, font=MAIN_FONT, width=22)
    issue_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Priority Level:", font=MAIN_FONT, fg=TEXT_COLOR, bg=PANEL_BACKGROUND).grid(row=3, column=0, padx=5, pady=5, sticky="w")
    priority_entry = tk.Entry(input_frame, font=MAIN_FONT, width=22)
    priority_entry.grid(row=3, column=1, padx=5, pady=5)

    add_button = tk.Button(
        input_frame,
        text="Add Ticket Record",
        font=BOLD_FONT,
        fg=DARK_BACKGROUND,
        bg=PRIMARY_ACCENT_COLOR,
        activebackground=SECONDARY_ACCENT_COLOR,
        activeforeground=DARK_BACKGROUND,
        command=add_gui_support_request
    )
    add_button.grid(row=4, column=0, columnspan=2, pady=10)

    # 3. Calculation Button
    button_frame = tk.Frame(window, bg=DARK_BACKGROUND)
    button_frame.pack(pady=10)

    clean_button = tk.Button(
        button_frame,
        text="Clean & Process CSV",
        font=BOLD_FONT,
        fg=DARK_BACKGROUND,
        bg=SECONDARY_ACCENT_COLOR,
        activebackground=PRIMARY_ACCENT_COLOR,
        activeforeground=DARK_BACKGROUND,
        command=run_gui_cleaning_process
    )
    clean_button.pack(side="left", padx=5)

    test_missing_button = tk.Button(
        button_frame,
        text="Test Missing File",
        font=BOLD_FONT,
        fg=DARK_BACKGROUND,
        bg=WARNING_ACCENT_COLOR,
        activebackground=PRIMARY_ACCENT_COLOR,
        activeforeground=DARK_BACKGROUND,
        command=test_missing_file_gui
    )
    test_missing_button.pack(side="left", padx=5)

    # 4. Output Display Section
    display_frame = tk.Frame(window, bg=PANEL_BACKGROUND, bd=2, relief="solid")
    display_frame.pack(pady=10, padx=15, fill="both", expand=True)

    stats_label = tk.Label(display_frame, text="Click 'Clean & Process CSV' to run inspection.", font=MAIN_FONT, fg=TEXT_COLOR, bg=PANEL_BACKGROUND, justify="left")
    stats_label.pack(anchor="w", padx=15, pady=10)

    error_label = tk.Label(display_frame, text="", font=MAIN_FONT, fg=WARNING_ACCENT_COLOR, bg=PANEL_BACKGROUND, justify="left", wraplength=420)
    error_label.pack(anchor="w", padx=15, pady=10)

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