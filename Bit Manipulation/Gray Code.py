__author__ = 'drzzh'

'''
    第n位的格雷码由两部分构成，一部分是n-1位格雷码，再加上 1<<(n-1)和n-1位格雷码的逆序的和。
    Time: O(N^2)
'''


class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        result = [0, 1]
        if n == 0:
            return [0]

        for i in range(2, n + 1):
            l = len(result)
            j = l - 1
            while j > -1:
                temp = 1 << (i - 1)
                result.append(result[j] + (temp))
                j -= 1
        return result
