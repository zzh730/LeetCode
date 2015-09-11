__author__ = 'drzzh'

'''
    modify in place trick: do not return any new array, use nums[:]

'''


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        n = len(nums)
        array = [0] * n
        if not k:
            return
        if k > n:
            k = k % n
        for i in range(k):
            array[i] = nums[-k + i]
        for i in range(n - k):
            array[k + i] = nums[i]
        nums[:] = array


'''
    做法是：
        nums.reverse()
        然后reverse前k个元素
        之后reverse剩余的
'''


class smartSolution():
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums.reverse()
        nums[:] = nums[k - 1::-1] + nums[:k - 1:-1]
        #        翻转0到k-1下标      翻转k到最后一个元素     -1就是倒着看


a = smartSolution()
print(a.rotate([1, 2, 3, 4], 2))
