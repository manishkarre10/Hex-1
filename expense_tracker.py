import pandas as pd
from datetime import datetime
import os

FILE_NAME = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])
    df.to_csv(FILE_NAME, index=False)

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Rent, etc.): ")
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    df = pd.read_csv(FILE_NAME)
    df.loc[len(df)] = [date, amount, category, description]
    df.to_csv(FILE_NAME, index=False)

    print("✅ Expense added successfully!\n")

def view_expenses():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses found.\n")
    else:
        print(df, "\n")

def category_summary():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No data available.\n")
    else:
        summary = df.groupby("Category")["Amount"].sum()
        print("\n📊 Category-wise Summary:")
        print(summary, "\n")

def monthly_summary():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No data available.\n")
    else:
        total = df["Amount"].sum()
        print(f"\n💰 Total Expenses This Month: ₹{total}\n")

def main():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
