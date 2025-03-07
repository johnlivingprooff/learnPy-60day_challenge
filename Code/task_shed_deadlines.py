'''
Exercise: Task Scheduler with Deadlines

Objective
Build a simple task management system that:
- Allows users to add tasks with deadlines.
- Displays all tasks along with the remaining time until each deadline.
- Removes completed or expired tasks automatically.
'''

from datetime import datetime

tasks = {}

def add_task():
    task_name = input("Enter the task name: ")
    deadline = input("Enter the deadline (YYYY-MM-DD HH:MM): ")

    try:
        datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        tasks[task_name] = deadline
        print(f'Task "{task_name}" added with deadline({deadline}) successfully!')
    except ValueError:
        print("Invalid deadline format. Please use YYYY-MM-DD HH:MM.")

def show_tasks():
    if not tasks:
        print("No tasks added yet!")
        return
    
    print("\nTasks:")
    for task, deadline in tasks.items():
        remaining_time = deadline - datetime.now()
        if remaining_time.total_seconds() > 0:
            print(f'Task: {task}, Deadline: {deadline}.\nRemaining Time: {remaining_time}')
        else:
            print(f'Task: {task}, Deadline: {deadline}.\nStatus: Expired!')

def remove_task():
    now = datetime.now()
    exp_tasks = [task for task, deadline in tasks.items() if deadline < now]
    for task in exp_tasks:
        del tasks[task]
    print(f'{len(exp_tasks)} expired tasks removed!')

def main():
    while True:
        print("\nTask Manager - Schedule\nSelect from option 1 - 3, or type '?' for help\n1. Add Task\n2. Show Tasks\n3. Remove Expired Tasks\n")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            break
        elif choice.lower() == 'exit':
            break
        elif choice == '?':
            print("Select 1 to add a task, 2 to show tasks, 3 to remove expired tasks, or type ''exit' to quit the app.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()