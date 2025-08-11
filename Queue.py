class Queue:
    def __init__(self):
        self.stack = []
    def enqueue(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0

    def dequeue(self):
        if not self.is_empty():
            return self.stack.pop(0)
        else:
            raise IndexError('Queue is empty')

    def size(self):
        return len(self.stack)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(
    'Size a queue: ', queue.size()
)

while not queue.is_empty():
    item = queue.dequeue()
    print(
        'Извлечен элемент: ', item
          )