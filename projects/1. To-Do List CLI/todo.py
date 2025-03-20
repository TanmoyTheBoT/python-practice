import os
import sys
import json

filename = "tasks.json"
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
jsonfile = os.path.join(script_dir, filename)

def load_tasks():
    if os.path.exists(jsonfile):
        try:
            with open(jsonfile, "r", encoding="utf-8") as file:
                content = file.read().strip()
                return json.loads(content).get("tasks", []) if content else []
        except (json.JSONDecodeError, FileNotFoundError):
            print("⚠️ Error: Corrupted JSON file. Resetting tasks...")
    return []

def save_tasks(tasks):
    with open(jsonfile, "w", encoding="utf-8") as file:
        json.dump({"tasks": tasks}, file, indent=4)

def view_tasks():
    clear_terminal()
    tasks = load_tasks()
    if tasks:
        print("\n📋 To-Do List:\n")
        print(f"{'No.':<4} {'Description':<40} {'Status':<12}")
        print("-" * 60)
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task.get("complete") else "❌"
            description = task.get("description", "No description")
            print(f"{index:<4} {description:<40} {status:<12}")
    else:
        print("\n🚀 No tasks found. Start by adding one!")

def add_task():
    clear_terminal()
    description = input("📝 Enter task description: ").strip()
    if description:
        tasks = load_tasks()
        tasks.append({"description": description, "complete": False})
        save_tasks(tasks)
        print(f"✅ Task '{description}' added successfully!")
    else:
        print("⚠️ Task description cannot be empty.")

def mark_complete_task():
    clear_terminal()
    tasks = load_tasks()
    if not tasks:
        print("\n⚠️  No tasks to complete.")
        return
    view_tasks()
    try:
        task_number = int(input("\n✅ Enter task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            if task["complete"]:
                print(f"⚠️  Task {task_number} is already marked as complete.")
            else:
                task["complete"] = True
                save_tasks(tasks)
                print(f"🎉 Task {task_number} marked as complete!")
        else:
            print(f"⚠️  Task number {task_number} does not exist.")
    except ValueError:
        print("⚠️  Invalid input. Please enter a valid task number.")


def delete_task():
    clear_terminal()
    tasks = load_tasks()
    if not tasks:
        print("\n⚠️  No tasks to delete.")
        return
    view_tasks()
    try:
        task_number = int(input("\n🗑️  Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"🗑️  Task '{removed_task['description']}' deleted successfully.")
        else:
            print(f"⚠️  Task number {task_number} does not exist.")
    except ValueError:
        print("⚠️  Invalid input. Please enter a valid task number.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_program():
    clear_terminal()
    print("👋 Goodbye! Have a productive day!")
    sys.exit(0)
    
def main():
    while True:
        try:
            print("\n📌 To-Do List Menu:")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Mark Task as Complete")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("\n🔹 Enter your choice: ").strip()
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
                exit_program()
            else:
                clear_terminal()
                print("⚠️  Invalid choice. Please enter a number between 1 and 5.")

        except KeyboardInterrupt:
            exit_program()

if __name__ == "__main__":
    main()
