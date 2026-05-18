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

def analyze_expenses(expenses):
    total_expense = 0
    highest_expense = 0
    highest_expense_name = ""
    cheapest_expense = 0
    cheapest_expense_name = ""
    category_expenses = {"Food": 0, "Utilities": 0, "Health": 0}

    for expense in expenses:
        total_expense += expense["amount"]
        print(f"Expense: {expense['name']}")
        print(f"Amount: ${expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print(f"Date: {expense['date']}\n")
        
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

analyze_expenses(expenses)