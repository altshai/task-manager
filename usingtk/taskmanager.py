import tkinter as tk
from tkinter import messagebox

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task_text = entry_task.get().strip()
    if task_text:
        tasks.append({"task": task_text, "completed": False})
        update_task_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete a selected task
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Function to mark a task as completed
def mark_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)  # Clear the listbox
    for task in tasks:
        status = "✔️" if task["completed"] else "❌"
        task_listbox.insert(tk.END, f'{status} {task["task"]}')

# Function to show help info
def show_help():
    messagebox.showinfo("Help", "Commands:\n- Add Task: Enter text and click 'Add Task'\n- Delete Task: Select a task and click 'Delete Task'\n- Complete Task: Select a task and click 'Mark Completed'")

# Function to exit the application
def exit_app():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x450")
root.resizable(False, False)

# Task Entry Section
frame_entry = tk.Frame(root)
frame_entry.pack(pady=10)

entry_task = tk.Entry(frame_entry, width=40)
entry_task.pack(side=tk.LEFT, padx=5)

btn_add = tk.Button(frame_entry, text="Add Task", command=add_task)
btn_add.pack(side=tk.RIGHT)

# Task Listbox
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Buttons for Task Actions
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

btn_complete = tk.Button(frame_buttons, text="Mark Completed", command=mark_completed)
btn_complete.grid(row=0, column=0, padx=5)

btn_delete = tk.Button(frame_buttons, text="Delete Task", command=delete_task)
btn_delete.grid(row=0, column=1, padx=5)

btn_help = tk.Button(frame_buttons, text="Help", command=show_help)
btn_help.grid(row=0, column=2, padx=5)

btn_exit = tk.Button(root, text="Exit", command=exit_app)
btn_exit.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
