def add_expense(expenses):
    while True:
        try:
            print("Enter an expense (name, amount, category, date): \n")
            expense_name = input("Name: \n")
            expense_amount = float(input("Amount: \n"))
            expense_category = input("Category: \n")
            expense_date = input("Date (YYYY-MM-DD): \n")

            new_expense = {
                "name": expense_name,
                "amount": expense_amount,
                "category": expense_category,
                "date": expense_date
            }
            expenses.append(new_expense)
            more_expenses = input("Do you want to add another expense? (yes/no): \n")
            if more_expenses.lower() != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter the correct data type for amount.")

def save_to_file(expenses, total_expense):
    try:
        file = open("expenses.txt", "w")
        file.write("Expense Name, Amount, Category, Date\n")
        for expense in expenses:
            file.write(f"{expense['name']}, {expense['amount']}, {expense['category']}, {expense['date']}\n")
        file.write("\nExpense Analysis:\n")
        file.write(f"Total Expense: ${total_expense:.2f}\n")
        file.close()
    except IOError:
        print("An error occurred while writing to the file.")

def calculate_expenses(expenses):
        total_expense = 0
        highest_expense = 0
        highest_expense_name = ""
        cheapest_expense = 0
        cheapest_expense_name = ""
        category_expenses = {}

        for expense in expenses:
            total_expense += expense["amount"]

            if (expense["category"] not in category_expenses):
                category_expenses[expense["category"]] = expense["amount"]
            else:
                category_expenses[expense["category"]] += expense["amount"]
            
            if expense["amount"] > highest_expense:
                highest_expense = expense["amount"]
                highest_expense_name = expense["name"]

            if cheapest_expense == 0 or expense["amount"] < cheapest_expense:
                cheapest_expense = expense["amount"]
                cheapest_expense_name = expense["name"]
        return total_expense, cheapest_expense_name, cheapest_expense, highest_expense_name, highest_expense, category_expenses

def display_summary(expenses,total_expense, cheapest_expense_name, cheapest_expense, highest_expense_name, highest_expense, category_expenses):
    for expense in expenses:
        print(f"Expense: {expense['name']}")
        print(f"Amount: ${expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print(f"Date: {expense['date']}\n")

    print(f"Total Expense: ${total_expense:.2f}")
    print(f"Average Expense:  ${total_expense/len(expenses):.2f}")
    print(f"Cheapest Expense: {cheapest_expense_name} - ${cheapest_expense:.2f}")
    print(f"Highest Expense: {highest_expense_name} - ${highest_expense:.2f}")
    for category, amount in category_expenses.items():
        print(f"Total spent on {category}: ${amount:.2f}")

    if total_expense > 200:
        print("You have exceeded your budget for this month!")
    else:
        print("You are within your budget for this month.")

expense1 = {
    "name": "Groceries",
    "amount": 150.00,
    "category": "Food",
    "date": "2024-06-01"
}
expense2 = {
    "name": "Electricity Bill",
    "amount": 75.00,
    "category": "Utilities",
    "date": "2024-06-02"
}
expense3 = {
    "name": "Gym Membership",
    "amount": 50.00,
    "category": "Health",
    "date": "2024-06-03"
}

expenses = [expense1, expense2, expense3]

add_expense(expenses)
total_expense, cheapest_expense_name, cheapest_expense, highest_expense_name, highest_expense, category_expenses = calculate_expenses(expenses)      
display_summary(expenses,total_expense, cheapest_expense_name, cheapest_expense, highest_expense_name, highest_expense, category_expenses)
save_to_file(expenses, total_expense)