todo_list = []

while True:
    print("\n--- To-Do Manager ---")
    print("1. View Tasks\n2. Add Task\n3. Exit")
    choice = input("Select an option (1-3): ")
    
    if choice == "1":
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("\nYour Current Tasks:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
    elif choice == "2":
        new_task = input("Enter the new task description: ")
        todo_list.append(new_task)
        print(f"Added task: '{new_task}'")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please select 1, 2, or 3.")
