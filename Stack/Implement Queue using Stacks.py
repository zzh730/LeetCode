__author__ = 'drzzh'


class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        self.stack = self.stack[1:]

    # @return an integer
    def peek(self):
        return self.stack[0]

    # @return an boolean
    def empty(self):
        return True if not self.stack else False
