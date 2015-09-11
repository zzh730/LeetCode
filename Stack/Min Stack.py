__author__ = 'drzzh'
'''
    用一个字典维护最小值,用count记录操作数, mindic存当前count里最小值
    Time: O(1)
    Space: O(n)

'''


class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.count = 0
        self.stack = []
        self.mindic = {}

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        self.count += 1
        if self.count == 1:
            self.mindic[1] = x
        elif self.mindic[self.count - 1] > x:
            self.mindic[self.count] = x
        else:
            self.mindic[self.count] = self.mindic[self.count - 1]

    # @return nothing
    def pop(self):
        self.stack.pop()
        self.count -= 1

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.mindic[self.count]


a = MinStack()
for item in [9, 10, 4, 3, 2, 6]:
    a.push(item)
    print(a.getMin())
a.pop()
print(a.getMin())
a.pop()
print(a.getMin())
a.pop()
print(a.getMin())
