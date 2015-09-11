__author__ = 'drzzh'

'''
    自己想的方法，就是backtracking加修枝， 如果某次产生的结果和之前的一样，那么就可以减掉这个
    注意一点：当出现重复的时候，只保留右子树的右子树， 因为右子树的左子树和左子树的右子树是一样
'''

class Solution1:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        n = len(nums)
        self.res = []
        nums.sort()
        self.dfs(nums, [], True)
        return self.res

    def dfs(self, nums, cur, flag):
        if not nums and flag:
            self.res.append(cur)
            return
        else:
            for index,i in enumerate(nums):
                if cur not in self.res and flag:
                    self.dfs(nums[index+1:], cur, flag)
                if cur + [i] not in self.res:
                    self.dfs(nums[index+1:], cur+[i], True)
                elif cur+[i] in self.res and nums:
                    self.dfs(nums[index+1:], cur+[i], False)

'''
    更好的办法是先排序，然后传整个数组，判断当前字符和之前的是否一样，一样了就略过
'''

class Solution:
    def subsetsWithDup(self, nums):
        self.res = []
        nums.sort()
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums, index, sub):
        self.res.append(sub)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, sub+[nums[i]])