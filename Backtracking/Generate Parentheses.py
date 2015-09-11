__author__ = 'drzzh'

'''
    backtracking就是dfs的加强版, 遇到有约束条件,要枚举全部解的题就往backtracking上靠

'''


class Solution:
    # @param {integer} n
    # @return {string[]}
    result = []

    def generateParenthesis(self, n):
        self.result = []
        if not n:
            return []
        self.dfs(0, 0, "", n)
        return self.result

    def dfs(self, left, right, temp, n):
        if left == right == n:
            self.result.append(temp)
            return
        elif left == n and right < n:
            self.dfs(left, right + 1, temp + ')', n)
        else:
            if left > right:
                self.dfs(left + 1, right, temp + '(', n)
                self.dfs(left, right + 1, temp + ')', n)
            else:
                self.dfs(left + 1, right, temp + '(', n)
