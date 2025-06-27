# 📝 Todo List CLI Application

This is a Python-based Command Line Interface (CLI) Todo List application that enables users to manage their tasks directly from the terminal. Tasks are stored persistently in a local `tasks.json` file.

---

## Features

- Add new tasks with a title, description, and due date
- View a list of all tasks
- Mark tasks as Pending, In Progress, or Completed
- Delete tasks by ID
- Display tasks that are due today
- Update existing task information
- Exit the application in a controlled manner

---

## Technologies Used

- **Python 3.x**
- **Built-in Python modules**:
  - `json` – for reading and writing task data
  - `time` – to handle delays and timestamps
  - `sys` – for application exit control
  - `datetime` – for date handling and comparison

---

## Project Structure


---

## 📄 File Descriptions

### `app.py`
- The **main script** users run to interact with the CLI app.
- Handles menu navigation, user input, and calls functions from `task.py` and `utils.py`.

### `task.py`
- Defines the `Task` class with properties like `id`, `title`, `description`, `due_date`, and `status`.
- May include task-related operations (e.g., load/save).

### `utils.py`
- Provides **helper functions** for input validation, formatting dates, generating unique task IDs, etc.

### `test_utils.py`
- Contains **unit tests** for verifying the correctness of utility functions.

### `tasks.json`
- Stores all tasks in **JSON format**.
- Acts as the app's local database.

### `.gitignore`
- Ensures files like `__pycache__/`, `venv/`, and logs aren't committed to Git.

### `app.log`
- Captures runtime logs, helpful for debugging or tracking issues.

---

Let me know if you'd like a full `README.md` combining this with your earlier app overview!


