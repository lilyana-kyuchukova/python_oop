from typing import List
from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = list()  # [[name, due_date],[name2, due_date..]]

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        count = 0

        for task in filter(lambda t: t.completed, self.tasks):
            self.tasks.remove(task)
            count += 1

        return f"Cleared {count} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]
        [result.append(t.details()) for t in self.tasks]

        return '\n'.join(result)

