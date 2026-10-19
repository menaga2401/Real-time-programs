#20th program-Expense tracker
expenses = []
while True:
    item = input("Enter expense name:")
    amount = float(input("Enter amount:"))
    expenses.append(amount)
    choice=input("Add another expense?(yes/no):")
    if choice == "no":
        break
print("\nYour Expenses:")

for amount in expenses:
    print(amount)
print("Total experience:",sum(expenses))
