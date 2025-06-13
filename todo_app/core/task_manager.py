# todo_app/core/task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(description)
        return True

    def get_all_tasks(self):
        return self.tasks
