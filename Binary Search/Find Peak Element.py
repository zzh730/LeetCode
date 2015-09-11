__author__ = 'drzzh'

'''
    提示用logn的算法，那只能是binary search了，
    注意一点， 特殊边界的判定：
                a > b
                a = b
                a+1 = b
'''


class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if not nums:
            return
        return self.bsearch(0, len(nums) - 1, nums)

    def bsearch(self, a, b, nums):
        if a > b:
            return
        mid = int((a + b) / 2)
        if a == b:
            return b
        if a + 1 == b:
            return a if nums[a] > nums[b] else b
        if nums[mid] >= nums[mid - 1] and nums[mid] >= nums[mid + 1]:
            return mid
        elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
            return self.bsearch(mid + 1, b, nums)
        elif nums[mid] < nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return self.bsearch(a, mid - 1, nums)
        else:
            return max(self.bsearch(a, mid - 1, nums), self.bsearch(mid + 1, b, nums))
