"""
    如果不用loop/recursion,就是数学解法.
    这种题就是写出大量的case,然后找规律
    注意: 0还有9的倍数-->corner case

    Time: O(1)
    Space: O(1)
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0
        return num % 9 if num % 9 else 9
