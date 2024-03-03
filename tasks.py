class Task:
    def __init__(self, description, dueDate, priority, category):
        self.description = description
        self.due_date = dueDate
        self.priority = priority
        self.category = category
        self.completed = False

    def __str__(self):
        status = "Open" if not self.completed else "Completed"
        return f"[{status}] {self.description} - Due: {self.due_date}, Priority: {self.priority}, Category: {self.category}"

    def mark_completed(self):
        self.completed = True

    def mark_open(self):
        self.completed = False
