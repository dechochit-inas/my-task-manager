# Task Manager CLI

A lightweight, terminal-based Python application designed to help you track, organize, and manage your daily task lists directly from the Windows Command Prompt (CMD).

## Features

- **Task Lifecycle Management:** Easily add, view, complete, and delete task entries.
- **Persistent Local Storage:** Automatically saves tasks to a local `tasks.json` file inside the `data/` directory.
- **Zero External Dependencies:** Built entirely using Python's standard library (`json`, `os`, `sys`).
- **Clean Architecture:** Modular code structure separating file I/O operations from core application logic.

## Project Structure

```text
my-task-manager/
│
├── data/
│   └── tasks.json          # Auto-generated runtime storage (ignored by git)
├── src/
│   ├── __init__.py         # Python package marker
│   ├── task_data.py        # File I/O operations & JSON handling
│   └── task_logic.py       # Core business logic for task CRUD operations
├── .gitignore              # Excludes venv, pycache, and runtime data
├── main.py                 # Application entry point & CLI menu
└── README.md               # Project documentation