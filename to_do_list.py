# Simple To-Do List Application
tasks = {}

def display_menu():
    print("\nTo-Do List Application")
    print("----------------------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task_name = input("Enter task name: ")
    if task_name:
        tasks[task_name] = "Pending"
        print(f"Task '{task_name}' added.")
    else:
        print("Task name cannot be empty.")

def view_tasks():
    if tasks:
        print("\nCurrent To-Do List:")
        for task, status in tasks.items():
            print(f"- {task}: {status}")
    else:
        print("\nNo tasks in the list.")

def update_task():
    task_name = input("Enter the task to update: ")
    if task_name in tasks:
        new_status = input("Enter new status (Pending/Completed): ")
        if new_status.lower() in ['pending', 'completed']:
            tasks[task_name] = new_status.capitalize()
            print(f"Task '{task_name}' updated to '{new_status.capitalize()}'.")
        else:
            print("Invalid status. Please enter 'Pending' or 'Completed'.")
    else:
        print("Task not found.")

# Function to delete a task
def delete_task():
    task_name = input("Enter the task to delete: ")
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' deleted.")
    else:
        print("Task not found.")

# Main program loop
while True:
    display_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
