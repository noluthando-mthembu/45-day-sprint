# 🎀 Interactive Transaction Analyzer App

A transaction summary application built for Windows 11 that processes customer spending records to compute Total, Average, Maximum, and Minimum values formatted in Rand (R).

---

## 💕 Key Features

* **Dual Interface (Single File):** Includes an interactive Terminal CLI menu and a Desktop GUI App with a startup launcher menu.
* **Dynamic Customer Entry:** Supports real-time entry of customer names, categories, and Rand (R) amounts.
* **Data Structure Integration:** Utilises `for` loops, lists (`list`), dictionaries (`dict`) for category frequencies, and sets (`set`) for unique category filtering.
* **Full Explicit Variables:** Written with un-abbreviated names (`customer_name`, `amount`, `category`, `total_value`, `maximum_value`, `minimum_value`, `average_value`, `category_counts`, `unique_categories`).
* **Custom Theme Pop-ups:** Floating `Toplevel` modal pop-up windows handle input errors and warnings.

---

## 🎨 Theme Styling

* **Title Label:** Neon Pink (`#ff7edb`)
* **Frame Background:** Dark Purple (`#2f2142`)
* **Accent Buttons:** Neon Cyan (`#36f9f6`) and Gold (`#fefe60`)
* **Font Family:** `Arial Rounded MT Bold`

---

## 📁 File Overview

* `transaction_analyser.py` — Main dual-interface application script.

---

## 💻 How to Run on Windows 11

1. Open VS Code terminal and navigate to folder:
   ```powershell
   cd budget_project\transaction_analyser