'''
Create a file-based to-do list app where users can add, remove, 
and view tasks. The app should store tasks in a text file.
'''

def add_task(task):
    try:
        with open('tasks.txt', 'a') as file:
            file.write(task + '\n')
        print(f"Task '{task}' added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_task(task):
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        
        with open('tasks.txt', 'w') as file:
            for t in tasks:
                if t.strip() != task:
                    file.write(t)
        print(f"Task '{task}' removed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("\nAll Tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t.strip()}")
            else:
                print("No tasks available.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    print("\nWelcome to To-Do list app:")
    while True:
        print("\n1. Add task\n2. Remove task\n3. View tasks\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            print("All Tasks:")
            view_tasks()
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            break
        elif choice == 'exit':
            break
        elif choice == 'quit':
            break
        elif choice == '?':
            print("\nTo use this app, select one of the 3 options:\n1. Add task\n2. Remove task\n3. View tasks\nType 'exit' or 'quit' to close the app.")
        else:
            print("Invalid choice, please select a valid option.")