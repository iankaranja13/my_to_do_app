import argparse
import logging
from datetime import datetime
from task import Task
from utils import load_tasks, save_tasks, generate_id

# Setup logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def add_task(title, description, due_date=None):
    try:
        tasks = load_tasks()
        task_id = generate_id(tasks)
        new_task = Task(id=task_id, title=title, description=description, due_date=due_date)
        tasks.append(new_task)
        save_tasks(tasks)
        logging.info(f"Added task: {title} with ID {task_id}")
        print(f"[✓] Task '{title}' added!")
    except Exception as e:
        logging.error(f"Failed to add task: {e}")
        print("[Error] Could not add task.")

def list_tasks(show_today_only=False):
    try:
        tasks = load_tasks()
        if show_today_only:
            today = datetime.today().date()
            tasks = [task for task in tasks if task.due_date == today.strftime("%Y-%m-%d")]
            logging.info(f"Listing tasks due today: {len(tasks)} found")
        else:
            logging.info(f"Listing all tasks: {len(tasks)} total")

        if not tasks:
            print("[!] No tasks found.")
            return

        for task in tasks:
            status = "✓" if task.completed else "✗"
            print(f"[{status}] {task.id}. {task.title} - {task.description} (Due: {task.due_date})")
    except Exception as e:
        logging.error(f"Failed to list tasks: {e}")
        print("[Error] Could not list tasks.")

def complete_task(task_id):
    try:
        tasks = load_tasks()
        for task in tasks:
            if task.id == task_id:
                task.mark_complete()
                save_tasks(tasks)
                logging.info(f"Task {task_id} marked as complete.")
                print(f"[✓] Task {task_id} marked as complete.")
                return
        logging.warning(f"Task ID {task_id} not found for completion.")
        print(f"[!] No task found with ID {task_id}.")
    except Exception as e:
        logging.error(f"Failed to complete task {task_id}: {e}")
        print("[Error] Could not complete task.")

def delete_task(task_id):
    try:
        tasks = load_tasks()
        updated_tasks = [task for task in tasks if task.id != task_id]

        if len(tasks) == len(updated_tasks):
            logging.warning(f"Task ID {task_id} not found for deletion.")
            print(f"[!] No task found with ID {task_id}.")
            return

        save_tasks(updated_tasks)
        logging.info(f"Task {task_id} deleted.")
        print(f"[✓] Task {task_id} deleted.")
    except Exception as e:
        logging.error(f"Failed to delete task {task_id}: {e}")
        print("[Error] Could not delete task.")

def main():
    parser = argparse.ArgumentParser(description="CLI To-Do List Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.add_argument("description", help="Description of the task")
    add_parser.add_argument("--due", help="Due date in YYYY-MM-DD format", default=None)

    # List tasks
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--today", action="store_true", help="List tasks due today only")

    # Complete task
    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("id", type=int, help="Task ID to mark as complete")

    # Delete task
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int, help="Task ID to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.description, args.due)
    elif args.command == "list":
        list_tasks(show_today_only=args.today)
    elif args.command == "complete":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        logging.warning("No command given. Use --help for usage info.")
        print("[!] No command provided. Use --help for guidance.")

if __name__ == "__main__":
    main()
