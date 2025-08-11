class TaskQueue:
    def __init__(self):
        self.stack = []

    def add_task(self, task):
        self.stack.append(task)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def get_next_task(self):
        if not self.is_empty():
            return self.stack.pop(0)
        return None

class Task:
    def __init__(self, name: str):
        self.name = name

queue = TaskQueue()

task1 = Task('Задача 1')
task2 = Task('Задача 2')
task3 = Task('Задача 3')

queue.add_task(task1)
queue.add_task(task2)
queue.add_task(task3)

next_task = queue.get_next_task()
print(f'Next task: {next_task.name if next_task else 'No tasks'}')

queue.get_next_task()

print(f'Queue is empty: {queue.is_empty()}')