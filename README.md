# Bank Management System

A robust, streamlit UI-based, if applicable Bank Management System implemented in Python. This project simulates the core functionalities of a banking application, allowing users to create accounts, deposit/withdraw funds, check balances, and manage transactions securely.

Designed with clean code practices, this project is ideal for understanding Object-Oriented Programming (OOP) concepts, file handling(or database integration), Exception handling and user authentication in Python.

## 🚀 Features

### User Features
*   **Account Creation:** Open a new bank account with a unique account number and initial deposit.
*   **Secure Login:** Access accounts using a secure account number and PIN/password.
*   **Deposit & Withdrawal:** Seamlessly add or remove funds with real-time balance updates and validation checks (e.g., preventing overdrafts).
*   **Balance Inquiry:** Check current account balances instantly.
*   **Transaction History:** View a log of past deposits, withdrawals, and transfers.
*   **Fund Transfer:** Securely transfer money between two accounts registered in the system.

### Admin Features
*   **View All Accounts:** Monitor all registered accounts and their details.
*   **Modify/Close Accounts:** Update account holder information or close accounts permanently.
*   **Search Account:** Quickly find specific account details using the account number.

---

## 🛠️ Tech Stack & Concepts Used

*   **Language:** Python 3.x
*   **Database/Storage:** 
    *   `JSON` file for lightweight file-based data persistence.
*   **Core Concepts:** 
    *   Object-Oriented Programming (OOPs) — Classes, Objects, Encapsulation.
    *   Exception Handling — Managing invalid inputs and runtime errors gracefully.
    *   Data Validation — Ensuring secure PIN creation and correct data formats.

---

## 📦 Project Structure

```text
├── src/
│   ├── main.py          # Application entry point
├── data/
│   └── accounts.db      # Database file (or accounts.csv)
├── README.md            # Project documentation
└── requirements.txt     # External dependencies (if any)