__author__ = 'drzzh'
"""
    two point解决
    start指向第一个0， i指向最后一个0，遇到非零元素每次交换start和i

    Time: O(n)
    Space: O(1)

"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return
        start = nums.index(0)
        if start == len(nums) - 1:
            return
        for i in range(start + 1, len(nums)):
            if nums[i] != 0:
                tp = nums[i]
                nums[i] = nums[start]
                nums[start] = tp
                start += 1
