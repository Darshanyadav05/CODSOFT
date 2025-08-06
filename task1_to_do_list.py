def display_menu():
    print("=== TO-DO LIST MENU ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return
    print("Your Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✔️" if task['done'] else "❌"
        print(f"{idx}. {task['task']} [{status}]")

def add_task(tasks):
    item = input("Enter the new task: ").strip()
    if item:
        tasks.append({'task': item, 'done': False})
        print("Task added successfully!")
    else:
        print("Empty task cannot be added.")

def mark_complete(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            idx = int(input("Enter the number of the task to mark as complete: "))
            if 1 <= idx <= len(tasks):
                tasks[idx-1]['done'] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            idx = int(input("Enter the number of the task to delete: "))
            if 1 <= idx <= len(tasks):
                deleted = tasks.pop(idx-1)
                print(f"Task '{deleted['task']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Thank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":

    main()
