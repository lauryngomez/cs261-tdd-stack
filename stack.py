# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# LAURYN GOMEZ


class Stack:
    DEFAULT_CAPACITY = 0

    def __init__(self, value = IndexError):
        self.capacity = self.DEFAULT_CAPACITY
        self.value = value
    
    def is_empty(self):
        return True

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty array')

    def peek(self):
        if self.is_empty():
            raise IndexError('peep from empty array')