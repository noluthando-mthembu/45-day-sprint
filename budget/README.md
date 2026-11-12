# 🌺 Personal Budget Manager App

A desktop financial calculator built for Windows 11 that computes net remaining balances after deducting expenses from monthly income in Rand (R).

---

## 💕 Key Features

* **Dual Interface Architecture:** Combines Terminal CLI and Desktop GUI interfaces with startup launcher switches.
* **Income & Expense Tracking:** Calculates net remaining balance in Rand (R) after evaluating total monthly expenses.
* **Defensive Input Handling:** Validates numeric input fields and displays custom `Toplevel` modal pop-up warnings on invalid entry.
* **Full Variable Naming:** Uses explicit variable names (`monthly_income`, `total_expenses`, `remaining_balance`, `expense_list`).

---

## 🎨 Theme Styling

* **Title Banner:** Neon Pink (`#ff7edb`)
* **Panel Frame:** Dark Purple (`#2f2142`)
* **Font Family:** `Arial Rounded MT Bold`

---

## 📁 File Overview

* `budget.py` — Main dual-interface budget manager script.
* `gui_budget.py` — Supporting GUI budget module.

---

## 💻 How to Run on Windows 11

1. Open VS Code terminal and navigate to folder:
   ```powershell
   cd budget_project\budget