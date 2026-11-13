💖 Mock ATM Login Simulator App

A security PIN authentication simulator built for Windows 11 that enforces a 3-attempt lockout boundary using defensive programming logic.

---

## 💕 Key Features

* **Dual Interface (Single File):** Contains both Terminal CLI mode and Desktop GUI mode in a single script.
* **Security Lockout Boundary:** Tracks failed authentication attempts and locks out the account after 3 incorrect entries.
* **Masked Entry Field:** Conceals typed PIN inputs using `*` characters for visual security.
* **Custom Security Pop-ups:** Displays custom floating `Toplevel` modal windows when account lockout triggers.
* **Full Explicit Variables:** Uses un-abbreviated variables (`correct_pin`, `maximum_attempts`, `attempts_used`, `account_locked`, `entered_pin`).

---

## 🎨 Theme Styling

* **Header Title:** Neon Pink (`#ff7edb`)
* **Warning Highlight:** Neon Yellow (`#fefe60`) / Red (`#ff5555`)
* **Background Frame:** Deep Slate (`#241b2f`)
* **Typography:** `Arial Rounded MT Bold`

---

## 📁 File Overview

* `login_simulator.py` — Main security simulator script.

---

## 💻 How to Run on Windows 11

1. Open VS Code terminal and navigate to folder:
   ```powershell
   cd budget_project\login_simulator