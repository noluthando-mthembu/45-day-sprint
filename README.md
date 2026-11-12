# 💖 45-Day Sprint Python Applications Portfolio

Welcome to my **45-Day Sprint Python Portfolio**! This repository showcases a suite of interactive, dual-interface desktop applications built for Windows 11. Each application provides both a **Terminal Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)** app built using Python's native `tkinter` library.

---

## 🎨 Design & Palette Palette

All applications and documentation follow a high-contrast **Pink & Neon Accent** theme:
* **Primary Pink:** `#ff7edb` (Neon Pink) / `#f38ba8` (Pastel Rose)
* **Complementary Cyan:** `#36f9f6` (Neon Cyan) / `#89b4fa` (Pastel Blue)
* **Accent Yellow:** `#fefe60` (Neon Gold)
* **Dark Background:** `#241b2f` (Deep Slate Purple)
* **Typography:** `Arial Rounded MT Bold`

---

## 📂 Project Suite Matrix

| Application Name | Subfolder | Primary Function | Key Features | Currency |
| :--- | :--- | :--- | :--- | :--- |
| **Support Request Data Cleaner** | `support_cleaner/` | Cleans support ticket CSV data and flags defects. | `csv.DictReader`, duplicate ID filtering, `try/except` traceback logs. | N/A |
| **Interactive Transaction Analyzer** | `transaction_analyser/` | Computes spending metrics and category counts. | `for` loops, lists, dictionaries, sets, dynamic input entries. | **R** (Rand) |
| **Transaction Categoriser** | `categoriser/` | Automatically categorises purchase items. | Keyword evaluation (`if/elif/else`), color-coded categories. | **R** (Rand) |
| **Personal Budget Manager** | `budget/` | Calculates net remaining monthly balance. | Income & expense tracking, defensive validation pop-ups. | **R** (Rand) |
| **Mock ATM Login Simulator** | `login_simulator/` | Simulates PIN authentication security. | 3-attempt lockout boundary, masked entry fields (`*`). | N/A |

---

## 🚀 How to Run Any Application on Windows 11

1. Open **VS Code** terminal panel.
2. Navigate into the specific project folder:
   ```powershell
   cd budget_project\<folder_name>
