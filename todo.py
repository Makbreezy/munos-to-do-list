tasks = []

def display_menu():
    print('\n--- TO DO LIST MENU ---')
    print('1. Add Task')
    print('2. View All Tasks')
    print('3. Mark All Tasks as Complete')
    print('4. Delete a Task')
    print('5. Exit')

def add_task():
    """Add a new task to the list"""
    task_text = input("Enter your task: ").strip()
    if task_text:
        # We append to the 'tasks' list, not the 'task_text' string
        tasks.append({"task": task_text, "completed": False})
        print(f"Task added: {task_text}")
    else:
        print("Task cannot be empty!")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty!")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "o"
        print(f"{index}. [{status}] {task['task']}")

def main():
    print("Welcome to your To-Do List")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            # Example logic for marking all complete
            for task in tasks:
                task["completed"] = True
            print("All tasks marked as complete!")
        elif choice == '4':
            print("Deleting a task functionality goes here...")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter 1-5")

if __name__ == "__main__":
    main()