class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def display_tasks(self):
        print("\nTask List:")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{index + 1}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}, Status: {status}")

    def mark_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.completed = True
            self.completed_tasks.append(task)
            self.tasks.pop(task_index)
            print(f"Task '{task.description}' marked as completed.")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, description, due_date, priority):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.description = description
            task.due_date = due_date
            task.priority = priority
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task.description}' removed.")
        else:
            print("Invalid task index.")

    def display_completed_tasks(self):
        print("\nCompleted Tasks:")
        for index, task in enumerate(self.completed_tasks):
            print(f"{index + 1}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Display Completed Tasks")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            priority = input("Enter priority (optional): ")
            todo_list.add_task(description, due_date, priority)

        elif choice == '2':
            todo_list.display_tasks()

        elif choice == '3':
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_as_completed(task_index)

        elif choice == '4':
            task_index = int(input("Enter the index of the task to update: ")) - 1
            description = input("Enter new task description: ")
            due_date = input("Enter new due date (optional): ")
            priority = input("Enter new priority (optional): ")
            todo_list.update_task(task_index, description, due_date, priority)

        elif choice == '5':
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            todo_list.remove_task(task_index)

        elif choice == '6':
            todo_list.display_completed_tasks()

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
