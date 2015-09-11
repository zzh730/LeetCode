__author__ = 'drzzh'

'''
    用俩队列, 一个temp暂存, count计数

'''
from collections import deque


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue3 = deque()
        self.queue = deque()
        self.count = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if len(self.queue3) != 0:
            self.queue3.popleft()
        self.queue3.append(x)
        self.queue.append(x)
        self.count += 1

    # @return nothing
    def pop(self):
        temp = deque()
        for i in range(self.count - 1):
            temp.append(self.queue.popleft())
        self.queue.popleft()
        self.count -= 1
        for i in range(self.count):
            x = temp.popleft()
            if i == self.count - 1:
                if len(self.queue3) != 0:
                    self.queue3.popleft()
                self.queue3.append(x)
            self.queue.append(x)

    # @return an integer
    def top(self):
        return self.queue3[0] if len(self.queue3) != 0 else None

    # @return an boolean
    def empty(self):
        return True if self.count == 0 else False


a = Stack()
for i in range(5):
    a.push(i)
    print(a.top())
for i in range(5):
    a.pop()
    print(a.top())
