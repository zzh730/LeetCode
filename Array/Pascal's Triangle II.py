__author__ = 'drzzh'

'''

'''


class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        prev = [1, 1]
        for i in range(2, rowIndex + 1):
            cur = [1]
            for j in range(1, i):
                cur.append(prev[j - 1] + prev[j])
            cur.append(1)
            prev = cur
        return prev
