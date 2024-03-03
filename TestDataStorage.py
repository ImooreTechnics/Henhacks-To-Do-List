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

def run_tests(test_data):
    for item in test_data:
        if "grade" in item:
            assignment = Assignment()
            assignment.addGrade(item["grade"])
            print(f"Assignment created: {assignment}")
        else:
            description = item["description"]
            due_date = item["due_date"]
            priority = item["priority"]
            category = item["category"]
            task = Task(description, due_date, priority, category)
            print(f"Task created: {task}")

def add_assignment_to_datastorage():
    # Load existing data from JSON file
    assignments = load_data_from_json('DataStorage.JSON')
    
    # Prompt user for assignment details
    description = input("Enter the assignment description: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    priority = input("Enter priority High/Medium/Low: ")
    category = input("Enter category: ")
    
    # Create a new assignment object
    new_assignment = {
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "category": category,
        "completed": False
    }
    
    # Add the new assignment to the list
    assignments.append(new_assignment)
    
    # Save the updated data back to JSON file
    save_data_to_json(assignments, 'DataStorage.JSON')
    print("Assignment added successfully!")

# Load test data from JSON file
test_data = load_data_from_json('DataStorage.JSON')

# Run tests
run_tests(test_data)

# Add a new assignment to the data storage
add_assignment_to_datastorage()