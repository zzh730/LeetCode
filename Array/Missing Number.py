__author__ = 'drzzh'

"""
    思路很简单，求和之后相减， 差的数就是
    当res == 0时，如果0在，就返回max num + 1
                 如果不在就返回0
    Time: O(n)
    Space: O(1)

"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        n = sum(range(m + 1))
        res = n - sum(nums)
        if res > 0:
            return res
        else:
            if 0 in nums:
                return m + 1
            else:
                return 0
