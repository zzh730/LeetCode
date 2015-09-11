__author__ = 'drzzh'
"""
    很容易出错的一点就是溢出，一定要考虑进去
    python int   [-2147483648,2147483647]

"""

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        flag = -1 if x < 0 else 1
        y = str(flag * x)
        new = ""
        for i in range(len(y)):
            new += y[len(y) - i - 1]
        result = int(new) * flag
        return result if result < 2147483648 and result > -2147483649 else 0



