from course import Assignment, Course
from tasks import Task


def main():
    while True:
        # Somehow display menu... display_menu()

        choice = input("Enter your choice: ")
        tasks = []

        if choice == "1":
            Task.add_task(tasks)
        elif choice == "2":
            Task.view_tasks(tasks)

        # Include other menu options and corresponding function calls


if __name__ == "__main__":
    main()
