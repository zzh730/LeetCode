__author__ = 'drzzh'

'''
    算法经典问题, 对于每个数两种选择, 选还是不选
'''


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}

    result = []

    def subsets(self, nums):
        self.result = []
        nums.sort()
        self.dfs([], nums)

        return self.result

    def dfs(self, lst, nums):
        if not nums:
            self.result.append(lst)
            return
        else:
            num = nums[0]
            self.dfs(lst, nums[1:])
            self.dfs(lst + [num], nums[1:])
