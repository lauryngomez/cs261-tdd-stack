# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# LAURYN GOMEZ


class Stack:


    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty array')
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError('peep from empty array')
        else:
            return self.items[0]

    def push(self, item):
        self.items.insert(0,item)