import json
import os
import logging
from task import Task

# Constants
TASKS_FILE = "tasks.json"

# Set up logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def load_tasks():
    """Load tasks from the tasks.json file."""
    try:
        if not os.path.exists(TASKS_FILE):
            logging.info("Task file not found. Returning empty task list.")
            return []
        with open(TASKS_FILE, "r") as f:
            data = json.load(f)
            tasks = [Task(**item) for item in data]
            logging.info(f"Loaded {len(tasks)} tasks.")
            return tasks
    except json.JSONDecodeError as e:
        logging.error(f"JSON decoding failed: {e}")
        print("[Error] Task data is corrupted.")
        return []
    except IOError as e:
        logging.error(f"Failed to read task file: {e}")
        print("[Error] Could not read tasks file.")
        return []
    except Exception as e:
        logging.critical(f"Unexpected error while loading tasks: {e}")
        print("[Error] Unexpected error occurred.")
        return []

def save_tasks(tasks):
    """Save tasks to the tasks.json file."""
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)
            logging.info(f"Saved {len(tasks)} tasks.")
    except IOError as e:
        logging.error(f"Failed to write to task file: {e}")
        print("[Error] Could not save tasks.")
    except Exception as e:
        logging.critical(f"Unexpected error while saving tasks: {e}")
        print("[Error] Unexpected error occurred while saving.")

def generate_id(tasks):
    """Generate a unique ID for a new task."""
    try:
        if not tasks:
            return 1
        new_id = max(task.id for task in tasks) + 1
        logging.debug(f"Generated new task ID: {new_id}")
        return new_id
    except Exception as e:
        logging.error(f"Failed to generate task ID: {e}")
        return 1  # fallback if something goes wrong
