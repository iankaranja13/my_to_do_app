from task import Task
import time
import sys

def main():
    """Interface for the Task Manager Application"""
    new_task = Task()
    file_path = "tasks.json"
    
    while True:
        choice = new_task.show_menu()
        
        match choice:
            case 1:
                new_task.task_title = input("Enter the task title: ")
                new_task.task_description = input("Enter the task description: ")
                new_task.task_due_date = input("Enter the due date (YYYY-MM-DD): ")
                new_task.create_task(new_task, file_path)
                print('''
                =========================================
                |                                        |
                |   Task has been created successfully   |
                |                                        |
                =========================================
                ''')
                time.sleep(2)

            case 2:
                new_task.view_all(file_path)
                time.sleep(2)

            case 3:
                new_task.mark_complete(file_path)
                time.sleep(2)

            case 4:
                new_task.delete_task_Id(file_path)

            case 5:
                tasks_due = new_task.tasks_due_today(file_path)
                print(tasks_due)

            case 6:
                new_task.update_task(file_path)

            case 7:
                print("Exiting the application. Thank you for using the Task Manager.")
                sys.exit()

if __name__ == "__main__":
    main()
