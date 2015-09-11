__author__ = 'drzzh'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        n = len(nums)
        start = -1
        end = -1
        left = 0
        right = n - 1
        first = False
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target and (mid == 0 or mid > 0 and nums[mid - 1] != target):
                start = mid
            if nums[mid] == target and (mid == n - 1 or mid < n - 1 and nums[mid + 1] != target):
                end = mid
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                temp = mid
                if not first:
                    tl = left
                    tr = right
                    first = True
                if start == -1:
                    left = tl
                    right = mid - 1
                    continue
                if end == -1:
                    right = tr
                    left = mid + 1
                    continue
                if start != -1 and end != -1:
                    return [start, end]
        return [start, end]
