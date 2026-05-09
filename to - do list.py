# To-Do List (CLI)

tasks = []


def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")


def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task():
    task = input("\nEnter the task to add: ")
    tasks.append(task)
    print("Task added successfully!")


def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


while True:
    show_menu()

    try:
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            view_tasks()

        elif choice == 2:
            add_task()

        elif choice == 3:
            delete_task()

        elif choice == 4:
            print("Exiting To-Do List... Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1 and 4.")

    except ValueError:
        print("Invalid input! Please enter a number.")
