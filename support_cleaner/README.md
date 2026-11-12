🌸 Support Request Data Cleaner App
A defensive Python application built for Windows 11 that cleans customer support ticket CSV files by flagging duplicate ticket identifiers, missing values, and malformed rows.
💕 Key Features
Dual Interface (Single File): Features an interactive Terminal CLI mode and a Desktop GUI App.
CSV Data Processing: Utilises csv.DictReader and csv.DictWriter to process tabular ticket data cleanly.
Defensive Exception Handling: Traps FileNotFoundError and empty file exceptions with traceback messages read from the bottom upwards.
Clean Output & Error Logging: Generates clean_support_requests.csv for valid records and error_report.csv for flagged defects.
Full Explicit Variable Naming: Written without shortcuts using full variable names (ticket_identifier, customer_name, issue_description, priority_level).
🎨 Theme Styling
Primary Title Header: Neon Pink (#ff7edb)
Background Frame: Deep Slate (#1e1e2e)
Success Accent: Pastel Green (#a6e3a1)
Warning Highlight: Pastel Rose (#f38ba8)
Font Family: Arial Rounded MT Bold
📁 File Overview
support_cleaner.py — Main dual-interface Python application script.
support_requests.csv — Raw input dataset.
clean_support_requests.csv — Clean output CSV containing verified tickets.
error_report.csv — Error log CSV detailing flagged ticket defects.
💻 How to Run on Windows 11
Open VS Code terminal and navigate to folder: cd budget_project\support_cleaner
Run application script: python support_cleaner.py
Choose interface mode: Enter 1 for Terminal CLI Mode or 2 for Desktop GUI Mode.
