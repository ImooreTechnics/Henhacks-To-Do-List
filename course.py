class Assignment:
    def __init__(self):
        self.grade = 0.0
        self.dueDate = "YYYY-MM-DD"
        self.weight = 0.0
        self.priority = 0

    def __init__(self, grade, dueDate, weight, priority):
        self.grade = grade
        self.dueDate = dueDate
        self.weight = weight
        self.priority = priority
    pass


class Course:
    def __init__(self, assignments, grade):
        self.assignments = assignments
        self.grade = grade

    def __str__(self):
        return f"{len(self.assignments)} assignments left.{self.grade}"

    def addAssignment(self, assignment):
        self.assignments.append(assignment)

    def removeAssignment(self, assignment):
        self.assignments.remove(assignment)

    pass
