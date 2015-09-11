__author__ = 'drzzh'

'''
    two pass可以用计数排序,
    one pass设red, blue俩指针, 一个指头,一个指尾,
        当i是red, 就交换, red++, i++
        i是blue, 也交换, blue++
        其他情况, i++

    Time: O(n)
    Space: O(1)

'''


class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        if not nums:
            return
        if len(nums) == 1:
            return
        i = 0
        red = 0
        blue = len(nums) - 1
        while i <= blue:
            if nums[i] == 0:
                self.switch(nums, red, i)
                red += 1
                i += 1
            elif nums[i] == 2:
                self.switch(nums, blue, i)
                blue -= 1
            else:
                i += 1
        return nums

    def switch(self, nums, x, y):
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp
        return y, x, nums


a = Solution()
