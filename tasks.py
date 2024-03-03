from course import Assignment
from task import Task

class Course:
    @staticmethod
    def gpaCalc(assignments):
        points = 0.0
        gradeVals = {
            "A": 4.0,
            "A-": 3.667,
            "B+": 3.333,
            "B": 3.0,
            "B-": 2.667,
            "C+": 2.333,
            "C": 2.0,
            "C-": 1.667,
            "D+": 1.333,
            "D-": 1.0,
            "F": 0.0
        }
        for i in assignments:
            points += gradeVals[i.grade]
        return points / len(assignments)

    def __init__(self, assignments):
        self.assignments = assignments
        self.grade = self.gpaCalc(assignments)

    def __str__(self):
        return f"{len(self.assignments)} assignments left.{self.grade}"

    def addAssignment(self, assignment):
        self.assignments.append(assignment)

    def removeAssignment(self, assignment):
        self.assignments.remove(assignment)


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
            status = "Open"

        print(
            f"{i + 1}. [{status}] {task.description} - Due: {task.due_date}, Priority: {task.priority}, Category: {task.category}")


if __name__ == "__main__":
    Trig = Assignment()
    Trig.addGrade("A")
    Calc = Assignment()
    Calc.addGrade("C-")
    Math = Course([Trig, Calc])
    print(Math.grade)

    tasks = []
    add_task(tasks)
    view_tasks(tasks)
