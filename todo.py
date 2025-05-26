import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "s") as file:
            return json.load(file)
    return []
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("✅ No tasks found!")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def mark_done(tasks):
    display_tasks(tasks)
    try:
        i = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]["done"] = True
            print("Marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input!")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        i = int(input("Enter task number to remove: ")) - 1
        if 0 <= i < len(tasks):
            tasks.pop(i)
            print("Task removed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input!")

def main():
    tasks = load_tasks()
    while True:
        print("\n📋 To-Do List\n1. View Tasks\n2. Add Task\n3. Mark as Done\n4. Remove Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
