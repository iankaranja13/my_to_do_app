from utils import load_file, save_file, update_task, format_date, task_id_generator, delete_task, notify_user_overdue, is_valid_date


class Task:
    def __init__(self):
        """Initialize a new task with default values."""
        self.task_id = None
        self.task_title = None
        self.task_description = None
        self.task_status = None
        self.task_due_date = None
        self.task_created_date = None
        self.task_status_updated_date = None

    def show_menu(self):
        
        print(
            """
            Greetings, Welcome to Our To do List App!
            Which service would you like to get today?
            
                1. Add a new task
                2. View all tasks
                3. Mark a task as complete
                4. Delete a task
                5. View tasks due today
                6. Update Task Data
                7. Exit
            """  
        )

        choice = int(input("Enter the service you would like to get: "))

        return choice

    def create_task(self, new_task, file_path):
        """Create a new task with user input."""
        # Load existing tasks from the file
        tasks = load_file(file_path)
        task_exist = False
        # Check if the task ID already exists
        for task in tasks:
            if int(task['task_id']) == new_task.task_id:
                task_exist = True
                break
        if task_exist:
            print("Task ID already exists. Please try again.")    
        else:
            self.task_id = task_id_generator(tasks)
            self.task_title = new_task.task_title
            self.task_description = new_task.task_description
            self.task_due_date = new_task.task_due_date
            while True:
                if is_valid_date(self.task_due_date):
                    break
                else:
                    print(" Invalid date. Please enter in yy-mm-dd format.")
                    self.task_due_date = input("Please enter the due date in the correct format: ")
            
            if self.task_due_date == format_date():
                self.task_status = "Due today"
            elif self.task_due_date < format_date():
                self.task_status = "Over Due"
            else:
                self.task_status = "Pending"
            self.task_created_date = format_date()
            self.task_status_updated_date = None

        tasks.append(self.to_dict())
        # Save the updated tasks back to the file
        save_file(file_path, tasks)

    def to_dict(self):
        """Convert task object to a dictionary for JSON saving."""
        return {
            "task_id": self.task_id,
            "task_title": self.task_title,
            "task_description": self.task_description,
            "task_status": self.task_status,
            "task_due_date": self.task_due_date,
            "task_created_date": self.task_created_date,
            "task_status_updated_date": self.task_status_updated_date
        }
    
    def __str__(self):
        """String representation of the task."""
        return (f"Task ID: {self.task_id}, Title: {self.task_title}, "
                f"Description: {self.task_description}, Status: {self.task_status}, "
                f"Due Date: {self.task_due_date}, Created Date: {self.task_created_date}, "
                f"Status Updated Date: {self.task_status_updated_date}")
    
    def update_task(self, file_path):
        """Update an existing task with new data."""
        try:
          update_task(file_path)
        except Exception as e:
            print(f" Error in update_task: {e}")

    def mark_complete(self, file_path):
        # Mark a task Complete
        try:
            task_id = input("Plese enter the id of the task that you want to update : ")
            tasks =  load_file(file_path)
            for task in tasks: 
                if task['task_id'] == int(task_id):
                    while True:
                        task_status = int(input("Enter task status: \n 1. Pending \n 2. In Progress \n 3. Completed \n:"))
                        match task_status:
                            case 1: 
                                task['task_status'] = "Pending"
                                print(f"✅ Task {task_id} marked as Pending.")
                                break
                            case 2: 
                                task['task_status'] = "In Progress"
                                print(f"✅ Task {task_id} marked as In Progress.")
                                break
                            case 3: 
                                if task['task_due_date'] == format_date():
                                    task['task_status']  = "Completed"
                                    print(f"✅ Task {task_id} marked as Complete.")
                                elif task['task_due_date']  < format_date():
                                    task['task_status']  = "Overdue-Completed" 
                                    print(f"✅ Task {task_id} marked as OverDue-Complete.")
                                break
                            case _: 
                                print("Invalid status. Please enter 1, 2, or 3.")
                            
                        save_file(file_path, tasks)
                    break  
        except Exception as e:
            print(f" Error in marking a task: {e}")
        
        save_file(file_path, tasks)

    def tasks_due_today(self, file_path):
        # Tasks that are due today
        
        try:
            tasks = load_file(file_path)
            due_today_tasks = []
            for task in tasks:
                if task['task_due_date'] == format_date():
                    due_today_tasks.append(task)
            if due_today_tasks == []:
                print("There are no tasks due today")
        except Exception as e:
            print(f" Error in listing tasks that are due today: {e}")
        return due_today_tasks
    
    def delete_task_Id(self, file_path):
        """Delete a task by ID with user input."""
        try:
            task_id = input("🗑️ Enter the ID of the task you want to delete: ").strip()
            
            if not task_id.isdigit():
                print(" Invalid ID. Please enter a numeric task ID.")
                return
            
            delete_task(task_id, file_path)
            
        except Exception as e:
            print(f" Error in deleting task: {e}")
    
    def view_all(self, file_name):
        tasks = load_file(file_name)
        for task in tasks:
            print (f'''
                   
                Task Id : {task["task_id"]}
                Ttask Title: {task["task_title"]}
                Task Description: {task["task_description"]}
                Task Status: {task["task_status"]}
                Task Due Date": {task["task_due_date"]}
                Task Created Date": {task["task_created_date"]}
                Task Status Updated Date": {task["task_status_updated_date"]}

            ''')