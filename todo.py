import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class Task:
    """
    Represents an individual task in a todo list
    """

    def __init__(self, description):
        """
        Instantiates a new task with description text
        created_on is automatically set and active is 
        default to True
        """
        self.description = description
        self.created_on = datetime.now()
        self.active = True

    def toggle(self):
        """
        Toggles the state of a task from active (pending)
        to inactive (done) and vice-versa.
        """
        logger.debug('toggling status...')
        self.active = not self.active

    def __repr__(self):
        return self.description


class TodoList:
    """
    Represents a todo list which contains todo tasks
    """

    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        """
        Creates a new task and adds it to the task list.
        """
        task = Task(description)
        self.tasks.append(task)
        return task

    def update_task(self):
        pass

    def remove_task(self):
        pass

    def toggle_task(self):
        pass

    def __repr__(self):
        return '\n'.join([task.description for task in self.tasks])
