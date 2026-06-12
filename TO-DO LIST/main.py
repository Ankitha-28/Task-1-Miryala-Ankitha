# ==============================
# TO-DO LIST APPLICATION
# DecodeLabs Project 1
# ==============================

tasks = []

while True:
    print("\n" + "=" * 30)
    print("      TO-DO LIST APP")
    print("=" * 30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Task
    if choice == "1":
        task_name = input("Enter task: ")

        task = {
            "id": len(tasks) + 1,
            "title": task_name
        }

        tasks.append(task)
        print("✅ Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("📌 No tasks available.")
        else:
            print("\nYour Tasks:")
            print("-" * 30)

            for task in tasks:
                print(f"{task['id']}. {task['title']}")

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("📌 No tasks available to delete.")
        else:
            print("\nCurrent Tasks:")
            for task in tasks:
                print(f"{task['id']}. {task['title']}")

            try:
                task_id = int(input("Enter Task ID to delete: "))

                found = False

                for task in tasks:
                    if task["id"] == task_id:
                        tasks.remove(task)
                        found = True
                        print("🗑️ Task deleted successfully!")
                        break

                if not found:
                    print("❌ Task ID not found.")

            except ValueError:
                print("❌ Please enter a valid number.")

    # Exit Program
    elif choice == "4":
        print("Thank you for using To-Do List App!")
        break

    # Invalid Choice
    else:
        print("❌ Invalid choice. Please select between 1 and 4.")