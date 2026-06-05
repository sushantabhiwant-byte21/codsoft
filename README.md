# To-Do List Application

A sleek, modern Python-based desktop application for managing your daily tasks. Built with `customtkinter`, this application provides a beautiful dark-mode interface and saves your tasks locally so you never lose track of what needs to be done.

## Features

- **Modern UI**: A visually appealing, responsive interface using `customtkinter`.
- **Add Tasks**: Quickly type and add tasks to your list.
- **Mark Complete**: Cross out completed tasks with a single click.
- **Delete Tasks**: Easily remove tasks you no longer need.
- **Persistent Storage**: Tasks are automatically saved to a local `tasks.json` file.

## Prerequisites

- Python 3.x installed on your machine.
- Pip (Python package installer).

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sushantabhiwant-byte21/codsoft.git
   cd codsoft
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```
   *(On macOS or Linux, you might need to use `python3 main.py`)*

## File Structure

- `main.py`: The main entry point containing the GUI implementation.
- `task_manager.py`: The backend logic for handling task creation, status updates, and saving/loading data.
- `requirements.txt`: Project dependencies.
- `tasks.json`: A generated file where your tasks are saved (ignored by git).

## License

This project is open-source and available under the MIT License.
