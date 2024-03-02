from course import Assignment

class Task:
    def __init__(self, description, due_date, priority, category):
        self.description = description
        self.dueDate = dueDate
        self.priority = priority
        self.category = category
        self.completed = False

def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")
    category = input("Enter category: ")
    tasks.append(Task(description, due_date, priority, category))
    print("Task added successfully!")


def view_tasks(tasks):
    print("To-Do List:")
    for i, task in enumerate(tasks):
        if task.completed:
            status = "Completed"  
        else:
            status = "Pending"

        print(f"{i+1}. [{status}] {task.description} - Due: {task.due_date}, Priority: {task.priority}, Category: {task.category}")