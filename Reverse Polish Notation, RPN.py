class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item: int):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

def reverse_polska_notation(s) -> int:
    my_stack = Stack()

    for item in s:
        if item == '*':
            result = my_stack.pop() * my_stack.pop()
            my_stack.push(result)

        elif item == '/':
            a = my_stack.pop()
            b = my_stack.pop()
            result = b / a
            my_stack.push(result)

        elif item == '-':
            a = my_stack.pop()
            b = my_stack.pop()
            result = a - b
            my_stack.push(result)

        elif item == '+':
            result = my_stack.pop() + my_stack.pop()
            my_stack.push(result)

        else:
            my_stack.push(int(item))

    return my_stack.items[0]

if __name__ == '__main__':
    test_s = input('Enter reverse polish notation: ')
    result = reverse_polska_notation(test_s)
    print(result)