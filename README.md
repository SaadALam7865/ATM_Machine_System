ProBank ATM System

Overview

ProBank ATM System is a Python-based console application simulating a banking ATM. It allows users to create accounts, authenticate, check balances, deposit, withdraw, change PINs, and delete accounts. Data is stored persistently in a JSON file (accounts.json). The system is designed to be simple, secure, and extensible, making it ideal for demonstrating banking system functionality.

Made & Designed by ❤️ Saad

Features





Account Creation: Create a new account with a unique account number, name, and 4-digit PIN.



Authentication: Secure login using account number and PIN.



Balance Check: View current account balance.



Deposit/Withdraw: Add or remove funds with validation for positive amounts and sufficient balance.



PIN Change: Update account PIN securely.



Account Deletion: Remove an account with confirmation.



Persistent Storage: Stores account data in accounts.json for persistence across sessions.

Requirements





Python 3.6 or higher



No external libraries required (uses standard json and os modules)

Installation





Clone the repository:

git clone https://github.com/your-username/probank-atm-system.git



Navigate to the project directory:

cd probank-atm-system

Usage





Ensure the account.py and bank_system.py files are in the same directory.



Run the main script:

python bank_system.py



Follow the console prompts to:





Create an account (option 1)



Log in with account number and PIN (option 2)



Perform actions like check balance, deposit, withdraw, change PIN, or delete account



Exit the system (option 3)

File Structure





account.py: Contains the Account class with methods for account operations (deposit, withdraw, etc.).



bank_system.py: Contains the BankSystem class and main menu logic for the ATM interface.



accounts.json: Auto-generated file to store account data persistently.

Example

🏦 Welcome to ATM Machine System
1. Create Account
2. Login to Account
3. Exit
Enter choice: 1
Enter Account Number: 101
Enter your name: Saad
Set 4-digit PIN: 1234
✅ Account created successfully!

Notes





Ensure the accounts.json file is writable in the project directory.



Account numbers must be unique.



PINs are stored as plain text in this version; consider hashing for production use.



The system is console-based, ideal for educational or demo purposes.

Contributing

Feel free to fork the repo and submit pull requests for improvements. For major changes, please open an issue to discuss.

License

This project is licensed under the MIT License.

Author

Saad - Made with ❤️ for secure banking solutions
