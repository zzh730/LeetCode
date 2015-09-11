__author__ = 'drzzh'

'''
    与一不同的是, 需要去重,  方法是排序加一个used字典, 第一个重复元素递归,第二个和之后都跳过

'''


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        self.result = []
        nums.sort()
        n = len(nums)
        dic = {}
        used = {}
        for index, i in enumerate(nums):
            dic[index] = i
            used[index] = False
        self.dfs([], n, dic, used)
        return self.result

    def dfs(self, lst, n, nums, used):
        if len(lst) == n:
            self.result.append(lst)
            return
        else:
            for i in nums:
                if used[i]:
                    continue
                if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                    continue
                used[i] = True
                num = nums[i]
                del nums[i]
                self.dfs(lst + [num], n, nums, used)
                nums[i] = num
                used[i] = False
