import json
import os

TODO_FILE = "todo_list.json"

def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_todo_list(todo_list):
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file)

def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def todo_list():
    todo_list = load_todo_list()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            todo_list.append(task)
            save_todo_list(todo_list)
            print(f"Task '{task}' added.")
        elif choice == '2':
            display_todo_list(todo_list)
        elif choice == '3':
            display_todo_list(todo_list)
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_index < len(todo_list):
                    removed_task = todo_list.pop(task_index)
                    save_todo_list(todo_list)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    todo_list()
