import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import task_data
import task_logic

def display_menu():
    print("\n--- Task Manager Menu ---\n1. Add Task\n2. List Tasks\n3. Complete Task\n4. Delete Task\n5. Exit\n-------------------------")

def main():
    tasks = task_data.load_tasks()
    while True:
        display_menu()
        choice = input("Enter choice (1-5): ").strip()
        if choice == '1':
            desc = input("Enter task description: ").strip()
            if desc: tasks = task_logic.add_task(tasks, desc)
        elif choice == '2':
            task_logic.list_tasks(tasks)
        elif choice in ('3', '4'):
            try:
                t_id = int(input("Enter Task ID: ").strip())
                tasks = task_logic.complete_task(tasks, t_id) if choice == '3' else task_logic.delete_task(tasks, t_id)
            except ValueError:
                print("Invalid input. Please enter a valid numerical ID.")
        elif choice == '5':
            task_data.save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break

if __name__ == "__main__":
    main()