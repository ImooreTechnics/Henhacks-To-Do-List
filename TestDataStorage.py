import json
from course import Assignment
from tasks import Task

def save_data_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def load_data_from_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

# Create some assignments
trig_assignment = Assignment()
trig_assignment.addGrade("A")

calc_assignment = Assignment()
calc_assignment.addGrade("C-")

# Create some tasks
task1 = Task("Complete trigonometry assignment", "2024-03-10", "High", "Math")
task2 = Task("Study for calculus exam", "2024-03-15", "High", "Math")
task3 = Task("Write essay on Shakespeare", "2024-03-20", "Medium", "English")
task4 = Task("Prepare presentation for history class", "2024-03-25", "Low", "History")

# Create a list of assignments and tasks
assignments_and_tasks = [trig_assignment.__dict__, calc_assignment.__dict__, task1.__dict__, task2.__dict__, task3.__dict__, task4.__dict__]

# Save the data to JSON file
save_data_to_json(assignments_and_tasks, 'DataStorage.json')

# Load the data from JSON file
loaded_data = load_data_from_json('DataStorage.json')

# Print the loaded data
for item in loaded_data:
    print(item)
