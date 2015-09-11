__author__ = 'drzzh'

'''
    递归时, nums得用新创建的, lst也是,不能修改了以后加入递归
'''


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    result = []

    def permute(self, nums):
        self.result = []
        if not nums:
            return []
        self.dfs([], set(nums))
        return self.result

    def dfs(self, lst, nums):
        if not nums:
            self.result.append(lst)
            return
        else:
            for digit in nums:
                temp = set(nums)
                temp.remove(digit)
                if not lst:
                    self.dfs([digit], temp)
                else:
                    self.dfs(lst + [digit], temp)


a = Solution()
print(a.permute([1, 2, 3]))
