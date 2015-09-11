__author__ = 'drzzh'

'''
    用到了修枝, 每次从用过的数字之后迭代,避免重复计算

'''


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    result = []

    def combine(self, n, k):
        self.result = []
        self.dfs(range(1, n + 1), k, [])
        return self.result

    def dfs(self, nums, k, lst):
        if k == 0:
            self.result.append(lst)
            return
        else:
            for index, digit in enumerate(nums):
                self.dfs(nums[index + 1:], k - 1, lst + [digit])


a = Solution()
print(a.combine(4, 2))
