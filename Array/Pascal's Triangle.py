__author__ = 'drzzh'

'''

'''


class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        res = [[1], [1, 1]]
        prev = [1, 1]
        if 0 < numRows < 3:
            return res[:numRows]
        elif not numRows:
            return []
        for i in range(3, numRows + 1):
            cur = [1]
            for j in range(1, i - 1):
                cur.append(prev[j - 1] + prev[j])
            cur.append(1)
            res.append(cur)
            prev = cur
        return res
