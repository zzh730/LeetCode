"""
    mark zeros and set zeros
    Time: O(mn)
    Space: O(m+n)
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_index = set([])
        col_index = set([])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_index.add(i)
                    col_index.add(j)

        for i in row_index:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in col_index:
            for i in range(len(matrix)):
                matrix[i][j] = 0
