__author__ = 'drzzh'

'''
    backtracking用dfs的方法: else里先循环, 判断, 修改temp结果,执行下一步dfs,之后把结果改回来即可.

    判断皇后合法的条件:
        用一位数组存, array[row] = col
        同行只有一个,
        只需遍历array, y != col,
        对角线上, 判断abs(y - lst[row]) == abs(x - row)!!!!!!!



'''
from copy import deepcopy


class Solution:
    # @param {integer} n
    # @return {integer}

    result = []
    result2 = []

    def solveNQueens(self, n):
        self.result = []
        self.result2 = []
        lst = {}
        for i in range(n):
            lst[i] = -100000
        self.dfs(0, n, n, lst)

        for res in self.result:
            board = []
            for row in range(n):
                str = ""
                queen = res[row]
                for col in range(n):
                    if col == queen:
                        str += "Q"
                    else:
                        str += "."
                board.append(str)
            self.result2.append(board)
        return self.result2

    def dfs(self, x, n, count, lst):
        if count == 0:
            new = deepcopy(lst)
            self.result.append(new)
            return
        else:
            for i in range(n):
                if self.vaild(x, i, lst):
                    lst[x] = i
                    self.dfs(x + 1, n, count - 1, lst)
                    lst[x] = -100000

    def vaild(self, x, y, lst):
        for row in lst:
            if lst[row] == y or abs(y - lst[row]) == abs(x - row):
                return False
        return True


a = Solution()
print(a.solveNQueens(8))
