# todo_app/core/task_manager.py
import json
import os

class TaskManager:
    def __init__(self, file_path='todo_app/data/tasks.json'):
        self.file_path = file_path
        self.tasks = self.load_tasks()
        self.next_id = max([task['id'] for task in self.tasks]) + 1 if self.tasks else 1

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description):
        task = {
            'id': self.next_id,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        return task

    def get_all_tasks(self):
        return self.tasks

    def mark_task_complete(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        initial_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        if len(self.tasks) < initial_len:
            self.save_tasks()
            return True
        return False
