__author__ = 'drzzh'


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        nodup = set()
        for num in nums:
            nodup.add(num)
        return True if len(nodup) < len(nums) else False
