class Assignment:
    def editAssignment(self):
        self.dueDate = input("Enter the due date (YYYY-MM-DD): ")
        self.priority = input("Enter priority High/Medium/Low: ")

    def __init__(self):
        self.grade = "A"
        self.dueDate = "YYYY-MM-DD"
        self.priority = "Unknown"
        self.editAssignment()

    def addGrade(self, grade):
        self.grade = grade


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
        return points/len(assignments)

    def __init__(self, assignments):
        self.assignments = assignments
        self.grade = self.gpaCalc(assignments)

    def __str__(self):
        return f"{len(self.assignments)} assignments left.{self.grade}"

    def addAssignment(self, assignment):
        self.assignments.append(assignment)

    def removeAssignment(self, assignment):
        self.assignments.remove(assignment)
