#To-Do List application
tasks = []  
def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Mark task as completed")
    print("5. Delete a task")
    print("6. Exit")

def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print(" No tasks found. Your list is empty.")
        return

    print("\nYour To-Do Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = " Done" if task["done"] else " Not Done"
        print(f"{index}. {task['task']} - {status}")

def update_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter new task description: ")
            tasks[task_no - 1]["task"] = new_task
            print(" Task updated successfully!")
        else:
            print(" Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as completed: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["done"] = True
            print(" Task marked as completed!")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            
            print(" Task deleted successfully!")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option 1-6: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print(" Thank you for using the To-Do List ")
        break
    else:
        print(" Invalid choice. Please try again.")