class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

def is_valid_stack_bracket(s: str) -> bool:
    my_stack = Stack()
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_pairs.values():
            my_stack.push(char)
        elif char in bracket_pairs:
            if my_stack.is_empty() or my_stack.pop() != bracket_pairs[char]:
                return False
        else:
            return False

    return my_stack.is_empty()

if __name__ == '__main__':
    test_s = input('Введите набор скобок для проверки: ')
    if is_valid_stack_bracket(test_s):
        print('Subsequence is True')
    else:
        print('Subsequence is False')