expenses = []
 
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input(" Choose an option: ")

    if choice == "1": 
        name = input("Expense name: ")
        amount = float(input("Amount: $"))

        expense = {
        "name": name,
        "amount": amount
      }

        expenses.append(expense)

        print("Expense added!")

    elif choice == "2":
      
        if len(expenses) == 0:
            print("No expenses found.")

        else: 
            for expense in expenses: 
                print(f"{expense['name']} - ${expense['amount']}")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total Expenses: ${total}")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
      