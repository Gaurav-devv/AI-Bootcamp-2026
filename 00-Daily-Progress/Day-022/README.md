# 🏦 Day 22 — Bank Management System

> **AI-Bootcamp-2026 | Python Journey**

A console-based **Bank Management System** built using Python.  
This project combines multiple Python concepts learned throughout the previous days into one practical application.

---

## 📅 Day Details

- **Day:** 22
- **Date:** 1 September 2026
- **Project:** Bank Management System
- **Language:** Python
- **Status:** ✅ Completed

---

## 🎯 Project Objective

The goal of this project was to apply Python fundamentals and OOP concepts to build a simple banking system.

The application allows users to perform basic banking operations such as:

- Create a bank account
- Deposit money
- Withdraw money
- View account details
- Update account information
- Store account information using JSON

---

## 🧠 Concepts Used

This project combines several concepts learned during the Python journey:

### Python Fundamentals

- Variables
- Data Types
- Input / Output
- Type Conversion
- Conditional Statements
- Loops
- Functions
- Lists
- Dictionaries
- String Operations

### Object-Oriented Programming

- Classes
- Objects
- Instance Methods
- `self`
- Encapsulation
- Constructor / `__init__`

### Error Handling

- `try`
- `except`
- `Exception`
- Handling `ValueError`
- Handling `KeyError`

### File Handling

- Reading files
- Writing files
- JSON
- `json.load()`
- `json.dump()`
- `pathlib.Path`
- Checking whether a file exists

---

## 🏗️ Project Structure

```text
02.BankManagement/
│
├── main.py
├── data.json
└── README.md
⚙️ Features
1. Create Account

Users can provide:

Name
Age
Email
PIN

The system generates an account number and initializes the balance to 0.

Basic validation is also performed before creating an account.

2. Deposit Money

Users can deposit money into their bank account.

The deposited amount is added to the existing account balance.

Example:

Current Balance: ₹1000
Deposit: ₹500

New Balance: ₹1500
3. Withdraw Money

Users can withdraw money from their account.

The system checks whether sufficient balance is available before completing the transaction.

Example:

Current Balance: ₹1500
Withdraw: ₹500

Remaining Balance: ₹1000
4. View Account Details

The user can view information such as:

Name
Age
Email
Account Number
Balance
5. Update Account Details

Users can update their existing account information.

For example:

Old Email:
old@example.com

New Email:
new@example.com
6. JSON Data Storage

Account information can be stored in a JSON file.

Example:

[
    {
        "Name": "Gaurav",
        "Age": 21,
        "Email": "gaurav@example.com",
        "Pin": "4532",
        "AccountNo.": 1234,
        "Balance": 0
    }
]

This allows the program to preserve data instead of losing everything when the program stops.

🔄 Program Flow
Start
  ↓
Load existing data from JSON
  ↓
Display Banking Menu
  ↓
User selects an option
  ↓
┌───────────────────────┐
│ 1. Create Account     │
│ 2. Deposit Money      │
│ 3. Withdraw Money     │
│ 4. Account Details    │
│ 5. Exit               │
│ 6. Update Details     │
└───────────────────────┘
  ↓
Perform selected operation
  ↓
Update stored data
  ↓
Return to menu / Exit
🧩 Important Code Concepts
Class

The banking functionality is organized inside a class:

class Bank:
    ...

This keeps related data and operations together.

Constructor

The __init__() method is used to initialize the object.

def __init__(self):
    ...
Dictionary

Account information is represented using a dictionary:

info = {
    "Name": "Gaurav",
    "Age": 21,
    "Email": "gaurav@example.com",
    "Pin": "4532",
    "AccountNo.": 1234,
    "Balance": 0
}
JSON

Python data can be converted into JSON and stored in a file.

json.dump(data, file)

And loaded again using:

data = json.load(file)
Exception Handling

The project uses exception handling to prevent the application from crashing when unexpected input or errors occur.

try:
    # code that may cause an error
except Exception as err:
    print(f"An exception occurred: {err}")
🐛 Debugging Lessons

During this project, I encountered and fixed errors such as:

ValueError

Example:

ValueError: invalid literal for int()

This happened when a non-numeric value was passed to int().

KeyError

Example:

KeyError: 'pin'

This happened because dictionary keys are case-sensitive.

For example:

"Pin"

and

"pin"

are different keys.

This helped reinforce the importance of carefully reading Python tracebacks.

💡 What I Learned

Through this project I learned how to:

Combine multiple Python concepts together
Design a small application using OOP
Work with dictionaries and lists
Store data using JSON
Read and write files
Validate user input
Handle runtime errors
Debug Python programs using tracebacks
Think about program flow before writing code
Convert individual concepts into a working project
🚀 Future Improvements

The current project is a beginner-level console application.

Possible improvements include:

Unique account number generation
Secure PIN handling
Login authentication
Transaction history
Multiple users
Better input validation
Better exception handling
Search account functionality
Delete account functionality
SQLite / MongoDB database
GUI interface
REST API using FastAPI
Authentication and authorization
📚 Learning Context

This project is part of my AI-Bootcamp-2026 Python journey.

The objective is not only to learn Python syntax but also to gradually develop the ability to build real-world applications independently.

✅ Status

Day 22 completed successfully! 🎉

From learning Python concepts individually → to combining them into a complete project.

👨‍💻 Author

Gaurav

Learning Python, AI, Generative AI, DSA and Full-Stack Development.

⭐ This project is part of my continuous learning journey toward becoming an AI Engineer.