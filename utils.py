from datetime import date
from datetime import datetime
import json

def load_file(file_name):
    """Load a JSON file and return its content."""
    try:
        with open(file_name, 'r') as f:
            task = json.load(f)
    except FileNotFoundError:
        print(f"File {file_name} not found. Creating a new task file.")
        task = []
    except json.JSONDecodeError as e:
        print(f" JSON decode error in '{file_name}': {e}")
        task = []
    return task

def save_file(file_name, task):
    """Save a JSON file with the given content."""
    try:
        with open(file_name, 'w') as f:
            json.dump(task, f, indent=4)
    except IOError as e:
        print(f" Error saving file '{file_name}': {e}")
    

def task_id_generator(tasks): 
    """Generate a unique task ID based on existing tasks."""
    try:
        if not tasks:
            return 1
        return max(task.get('task_id', 0) for task in tasks) + 1
    except Exception as e:
        print(f"Error in task_id_generator: {e}")
        return 1

        
def format_date():
    try:
        return date.today().strftime('%Y-%m-%d')
    except Exception as e:
        print(f" Error in format_date: {e}")

def notify_user_overdue(task_due_date):
    """Notify the user if a task is overdue."""
    try:
        today = date.today().strftime('%Y-%m-%d')
        if task_due_date < today:
            print(f"Task due date {task_due_date} is overdue!")
    except Exception as e:
        print(f" Error in notify_user_overdue: {e}")

def delete_task(task_id, file_path):
    """Delete a task by its ID."""
    try:
        deleted = False
        tasks = load_file(file_path)
        for task in tasks:
            if task['task_id'] == int(task_id):
                index_task = tasks.index(task)
                del tasks[index_task]
                deleted = True
                break 
            else: print(f"Task with ID {task_id} not found.")
        
        if deleted:
            print(f"Task with ID {task_id} deleted successfully.")
            save_file(file_path, tasks)
    except Exception as e:
        print(f" Error in delete_task: {e}")

def update_task(file_path):
    """Update Task."""
    try:
        task_id = input("Please enter the id of the task that you want to update: ")
        print(
            '''
                  What Would You Like to Update?
                    1. Task Title
                    2. Task Description
                    3. Task Status
                    4. Task Due Date
                    5. All
                    6. Exit
        '''
        )

        tasks = load_file(file_path)
        choice = input("Enter your choice (1-6): ")
        for task in tasks:
            if task["task_id"] == int(task_id):
                match choice:
                    case '1':
                        task['task_title'] = input("Enter new task title: ")
                        task['task_status_updated_date'] = format_date()
                    case '2':
                        task['task_description'] = input("Enter new task description: ")
                        task['task_status_updated_date'] = format_date()
                    case '3':
                        task['task_status'] = input("Enter new task status: ")
                        task['task_status_updated_date'] = format_date()
                    case '4':
                        task['task_due_date'] = input("Enter new task due date (YYYY-MM-DD): ")
                        task['task_status_updated_date'] = format_date()
                    case '5':
                        task['task_title'] = input("Enter new task title: ")
                        task['task_description'] = input("Enter new task description: ")
                        task['task_status'] = input("Enter new task status: ")
                        task['task_due_date'] = input("Enter new task due date (YYYY-MM-DD): ")
                        task['task_status_updated_date'] = format_date()
                    case '6':
                        print("Exiting update process.")
                        return
                    case _:
                        print("Invalid choice. Please try again.")
                       
                save_file(file_path, tasks)
                print(f"Task with ID {task_id} updated successfully.")
            break
        else: print(f"Task with ID {task_id} not found.") 
    except Exception as e:
        print(f" Error in update_task_status: {e}")

def is_valid_date(date_str):
    try:
        # Try to parse the date with the format yy-mm-dd
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False




