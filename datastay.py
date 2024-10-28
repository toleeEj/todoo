def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f'Task "{task}" added!')

def view_tasks(tasks):
    if tasks:
        print("Your tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks found.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter the task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed_task = tasks.pop(idx)
            print(f'Task "{removed_task}" deleted!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

tasks = load_tasks()
while True:
    action = input("Choose an action - [A]dd, [V]iew, [D]elete, [Q]uit: ").upper()
    if action == 'A':
        add_task(tasks)
    elif action == 'V':
        view_tasks(tasks)
    elif action == 'D':
        delete_task(tasks)
    elif action == 'Q':
        save_tasks(tasks)
        print("Tasks saved. Goodbye!")
        break
    else:
        print("Invalid option.")
