import tkinter as tk
from tkinter import messagebox

# Load and save tasks from a file
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

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Task Added", f'Task "{task}" added!')
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to display tasks in the listbox
def update_task_list():
    task_list.delete(0, tk.END)
    for idx, task in enumerate(tasks, start=1):
        task_list.insert(tk.END, f"{idx}. {task}")

# Function to delete a selected task
def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        idx = selected_task_index[0]
        removed_task = tasks.pop(idx)
        update_task_list()
        messagebox.showinfo("Task Deleted", f'Task "{removed_task}" deleted!')
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Load initial tasks
tasks = load_tasks()

# Set up the main application window
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x300")

# Input field for new tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Button to add a task
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)
update_task_list()

# Button to delete a selected task
delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_button.pack(pady=5)

# Function to save tasks on exit
def on_close():
    save_tasks(tasks)
    root.destroy()

# Configure the close event to save tasks before exiting
root.protocol("WM_DELETE_WINDOW", on_close)

# Run the application
root.mainloop()
