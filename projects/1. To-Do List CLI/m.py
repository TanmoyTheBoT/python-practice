import json
import os


jsonfile = "tasks.json"


def load_tasks():
    if os.path.exists(jsonfile):
        with open(jsonfile, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if content:
                return json.loads(content).get("tasks", [])
    return []

def save_tasks(tasks):
    with open(jsonfile, "w", encoding="utf-8") as file:
        json.dump({"tasks": tasks}, file, indent=4)

def view_tasks():
    clear_terminal()
    tasks = load_tasks()
    if tasks:
        print("\nTo-Do List:\n")
        print("{:<4} {:<40} {:<12}".format("No.", "Description", "Status"))
        print("-" * 56)
        for index, task in enumerate(tasks, start=1):
            status = "Complete" if task.get("complete") else "Incomplete"
            print("{:<4} {:<40} {:<12}".format(index, task.get('description'), status))
    else:
        print("\nNo tasks found.")

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
        task_number = int(input("\nEnter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            if task["complete"]:
                print(f"Task {task_number} is already marked as complete.")
            else:
                task["complete"] = True
                save_tasks(tasks)
                print(f"Task {task_number} marked as complete.")
        else:
            print(f"Task number {task_number} does not exist.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def delete_task():
    clear_terminal()
    tasks = load_tasks()
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['description']}' deleted successfully.")
        else:
            print(f"Task number {task_number} does not exist.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        print("\nTo-Do List Menu:")
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
            print("bye")
            break
        else:
            clear_terminal()
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
