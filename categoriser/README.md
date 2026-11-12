# Transaction Categoriser App

A dual-interface Python application built for Windows 11 that automatically categorises transaction descriptions into spending groups (Groceries, Transport, Utilities, and Other Spending) with Rand (R) currency formatting.

---

## Key Features

* **Dual Interface (Single File):** Choose between an interactive Terminal Command-Line Interface (CLI) or a Desktop Graphical User Interface (GUI) app upon launching.
* **Keyword Categorisation:** Uses Python conditional branches (`if / elif / else`) to evaluate text keywords.
* **Custom Pop-up Dialogs:** Uses floating `Toplevel` modal windows for input errors and validation warnings.
* **Explicit Variable Naming:** Code written without shortcuts using full variable names (`customer_name`, `amount`, `category`, `transaction_list`).
* **Visual Styling:** Desktop GUI formatted with **Arial Rounded MT Bold** typography and color-coded labels.

---

## File Overview

* **Script File:** `categoriser.py`
* **Target Directory:** `C:\Users\nolut\budget_project\categoriser`

---

## How to Run on Windows 11

1. Open VS Code terminal and navigate to folder:
   ```powershell
   cd budget_project\categoriser