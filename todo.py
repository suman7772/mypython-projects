class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                status = ' [X]' if task['completed'] else ' [ ]'
                print(f"{idx}. {task['description']}{status}")

    def add_task(self, description):
        self.tasks.append({'description': description, 'completed': False})
        print("Task added successfully!")

    def mark_task_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def update_task(self, task_number, new_description):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['description'] = new_description
            print("Task description updated.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task removed.")
        else:
            print("Invalid task number.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Update Task Description")
        print("5. Remove Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '3':
            task_num = int(input("Enter task number to mark as completed: "))
            todo_list.mark_task_completed(task_num)
        elif choice == '4':
            task_num = int(input("Enter task number to update: "))
            new_description = input("Enter new task description: ")
            todo_list.update_task(task_num, new_description)
        elif choice == '5':
            task_num = int(input("Enter task number to remove: "))
            todo_list.remove_task(task_num)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
