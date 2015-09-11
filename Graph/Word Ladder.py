__author__ = 'drzzh'

'''
图搜索的一道题：
    把每个词看成一点，把俩词相差字母个数当成两点的距离，bfs找最小
    有两种解法：1. 对dict迭代，比较两个词，相差为1就添加到neighbor，TIME : O (n*L) 当字典很大时，不划算
              2. 遍历这个词的每个字母， 对除自己意外的25个字母遍历，如果新词在dict里，就添加到neighbor里， Time: O(25*L)

    注意： 1. 把end添加到dict
          2. 访问过的节点，在dict删除即可
          3. queue里装节点以及level数

'''

import string
from collections import deque


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dic):
        dict = {}
        for item in dic:
            dict[item] = True
        dict[end] = True
        queue = deque([(start, 1)])
        while queue:
            cur, lvl = queue.popleft()
            if cur == end:
                return lvl
            neighbors = self.findNeighbors(cur, dict)
            for item in neighbors:
                queue.append((item, lvl + 1))
        else:
            return 0


    def findNeighbors(self, start, dict):
        letters = string.ascii_lowercase
        neighbors = []
        for index,item in enumerate(start):
            for letter in letters:
                if item != letter:
                    newWord = start[:index]+letter+start[index+1:] #tricky, do not ust string.replace, may cause multiple replacement
                    if newWord in dict:
                        neighbors.append(newWord)
                        del dict[newWord]
        return neighbors


start = "leet"
end = "code"
dict = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]

a = Solution()
print(a.ladderLength(start, end, dict))
