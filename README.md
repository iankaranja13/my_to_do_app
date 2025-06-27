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

project-root/
│
├── task.py # Contains the Task class and task operations
├── main.py # Entry point of the application
├── tasks.json # Stores all task data in JSON format
├── app.log # Log file capturing task-related activity
└── README.md # Project documentation

