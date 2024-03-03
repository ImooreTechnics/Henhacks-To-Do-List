class Task:
    def __init__(self, description, dueDate, priority, category):
        self.description = description
        self.due_date = dueDate
        self.priority = priority
        self.category = category
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Open"
        return f"[{status}] {self.description} - Due: {self.due_date}, Priority: {self.priority}, Category: {self.category}"

    def mark_completed(self):
        self.completed = True

    def mark_open(self):
        self.completed = False

'''
In the modified Task.py, I've renamed the dueDate parameter to 
 to match. I've also added
   mark_completed and mark_open methods to allow for marking tasks 
   as completed or open.
'''