
"""
    解法很简单，从1，2，3，4开始枚举结果，发现规律就出来了
    思路是，把必输的情况给对手你就赢了

    Time: O(1)
    Space: O(1)

"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n%4)!=0