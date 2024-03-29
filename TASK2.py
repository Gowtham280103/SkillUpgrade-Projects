def display_tasks(tasks):
    print("\nYour To-Do List:")
    if not tasks:
        print("No tasks yet!")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. [{task['status']}] {task['description']}")
    print()

def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append({'description': description, 'status': 'Incomplete'})
    print("Task added successfully!")


def mark_completed(tasks):
    display_tasks(tasks)
    index = int(input("Enter the index of the completed task: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]['status'] = 'Completed'
        print("Task marked as completed!")
    else:
        print("Invalid task index!")


def main():
    tasks = []

    while True:
        print("\n1. Display Tasks\n2. Add Task\n3. Mark Completed\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
