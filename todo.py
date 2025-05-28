import json
import os
from datetime import datetime

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5.Mark Task as Uncompleted")
        print("6. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            print("Add Task feature not implemented yet.")
        elif choice == "2":
            print("View Tasks feature not implemented yet.")
        elif choice == "3":
            print("Delete Task feature not implemented yet.")
        elif choice == "4":
            print("Mark Task as Completed feature not implemented yet.")
        elif choice == "5":
            print("Mark Task as Uncompleted feature not implemented yet.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()