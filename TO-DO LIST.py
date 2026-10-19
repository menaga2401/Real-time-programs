tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("Your To-Do List:")
        for task in tasks:
            print("-", task)

    elif choice == "3":
         print("Thank you!")
         break

    else:
        print("Invalid choice!")



