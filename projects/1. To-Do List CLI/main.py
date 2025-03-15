import json
import os
from rich.console import Console
from rich.table import Table

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r", encoding="utf-8") as file:
            content = file.read().strip()
            if content:
                return json.loads(content).get("tasks", [])
    return []

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump({"tasks": tasks}, f, indent=4)

def view_tasks():
    clear_terminal()
    tasks = load_tasks()
    console = Console()
    if tasks:
        table = Table(title="To-Do List")
        table.add_column("No.", style="dim", width=4)
        table.add_column("Description", min_width=30, overflow="fold")
        table.add_column("Status", justify="center", width=12)
        for index, task in enumerate(tasks, start=1):
            status = "Complete" if task.get("complete") else "Incomplete"
            table.add_row(str(index), task.get('description', ''), status)
        console.print(table)
    else:
        console.print("[bold red]No tasks found.[/bold red]")

def add_task():
    clear_terminal()
    description = input("Add your task description: ").strip()
    if description:
        tasks = load_tasks()
        new_task = {
            "description": description,
            "complete": False
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task description cannot be empty.")

def mark_complete_task():
    clear_terminal()
    tasks = load_tasks()
    view_tasks()
    try:
        task_no = int(input("\nEnter the task number to mark as complete: "))
        if 1 <= task_no <= len(tasks):
            task = tasks[task_no - 1]
            if task["complete"]:
                print(f"Task {task_no} is already marked as complete.")
            else:
                task["complete"] = True
                save_tasks(tasks)
                print(f"Task {task_no} marked as complete.")
        else:
            print(f"Task number {task_no} is out of range.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def delete_task():
    clear_terminal()
    tasks = load_tasks()
    view_tasks()
    try:
        task_no = int(input("\nEnter the task number to delete: "))
        if 1 <= task_no <= len(tasks):
            task = tasks.pop(task_no - 1)
            save_tasks(tasks)
            print(f"Task '{task['description']}' deleted successfully.")
        else:
            print(f"Task number {task_no} is out of range.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        print("\nOptions:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            clear_terminal()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
