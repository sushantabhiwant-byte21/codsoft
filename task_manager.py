import json
import os
import uuid

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description):
        task = {
            "id": str(uuid.uuid4()),
            "description": description,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def get_tasks(self):
        return self.tasks

    def update_task_status(self, task_id, completed):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = completed
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        if len(self.tasks) < initial_length:
            self.save_tasks()
            return True
        return False
