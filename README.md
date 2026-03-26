# TrackMySpend – Student Expense Tracker

## Live Application

You can access the deployed web application here:

https://trackmyspend.streamlit.app

---

## Project Description

TrackMySpend is a web-based student expense tracking application built using Python and Streamlit. It allows users to manage daily expenses, set budgets, and monitor spending in real time.

This version of the application supports multiple users, where each user can securely manage their own data.

---

## Problem Statement

Many students find it difficult to track their daily spending. Small expenses such as food, travel, or stationery often go unnoticed, which can lead to overspending.

Without a proper system, students may lose control of their budget and find it difficult to understand where their money is being spent.

---

## Proposed Solution

TrackMySpend provides a simple system where users can record and monitor their expenses. Each user can set a budget, add expense details, and view their total spending.

The system calculates the remaining budget automatically and ensures that each user’s data is stored separately.

---

## Features

- User login and signup system
- Multi-user support
- Set and manage personal budget
- Add daily expenses with category and notes
- View all recorded expenses
- Calculate total spending
- Display remaining budget
- Clear expense history

---

## Technologies Used

- Python
- Streamlit
- Pandas
- SQLite

---

## Project Structure

student-expense-tracker/
│
├── app.py
├── auth.py
├── expense_manager.py
├── requirements.txt
├── README.md
│
└── data/
    └── data.db

---

## Installation

Install the required libraries:

pip install -r requirements.txt

---

## Running the Application

Run the following command:

streamlit run app.py

---

## Usage

1. Create an account or login.
2. Set your monthly budget.
3. Add expense details including date, category, amount, and notes.
4. View all expenses.
5. Track total spending and remaining budget.

---

## Learning Outcome

This project demonstrates:

- Multi-user application development
- Database integration using SQLite
- Session management
- Modular programming in Python
- Web app development using Streamlit

---

## Conclusion

TrackMySpend helps students monitor their spending habits and maintain better control over their finances. It provides a simple and practical solution for managing daily expenses using Python and Streamlit.
