__author__ = 'drzzh'
'''
又是一道字符串问题用图算法解决的问题
把board看成图，找到第一个字符然后DFS，
    需要注意的是：
        1. 图的构建，可以加上边框，这样就能避免边界讨论
        2. stack里存坐标，还有word的index
        3. recursion的边界条件，index == len(word)

'''

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not word:
            return True
        m = len(board)
        n = len(board[0])
        graph = [['.' for i in range(n + 2)]]
        for string in board:
            string = list(string)
            string.insert(0, '.')
            string.append('.')
            graph.append(string)
        graph.append(['.' for i in range(n + 2)])
        stack = self.findFirstChar(graph, word[0])
        result = False
        while stack:
            x, y, index = stack.pop()
            result = self.dfs(x, y, index, word, graph)
            if result:
                return result
        return result

    def findFirstChar(self, graph, chr):
        result = []
        for index1, item in enumerate(graph):
            for index2, c in enumerate(item):
                if c == chr:
                    result.append((index1, index2, 0))

        return result

    def dfs(self, x, y, index, word, graph):
        if index == len(word):
            return True
        if graph[x][y] != word[index] or graph[x][y] == '.':
            return False
        else:
            temp = graph[x][y]                                       #trick here, need to restore the visited point
            graph[x][y] = '.'
            res = self.dfs(x - 1, y, index + 1, word, graph) or \
                  self.dfs(x + 1, y, index + 1, word, graph) or \
                  self.dfs(x, y + 1, index + 1, word, graph) or \
                  self.dfs(x, y - 1, index + 1, word, graph)
            graph[x][y] = temp                                      #tricky
            return res

    def printGraph(self, graph):
        for i in graph:
            print(i)
            print()


board = ['ab']
word = "ab"
a = Solution()
print(a.exist(board, word))
