__author__ = 'drzzh'


class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        result = []
        if not nums:
            return [""]
        n1 = 0
        n2 = 1
        while n2 < len(nums):
            if nums[n2] == nums[n2 - 1] + 1:
                n2 += 1
            elif nums[n2] > nums[n2 - 1] + 1:
                if n2 - 1 != n1:
                    result.append(str(nums[n1]) + "->" + str(nums[n2 - 1]))
                else:
                    result.append(str(nums[n1]))
                n1 = n2
                n2 += 1
        if n2 == len(nums):
            if n2 - 1 != n1:
                result.append(str(nums[n1]) + "->" + str(nums[n2 - 1]))
            else:
                result.append(str(nums[n1]))
        return result


a = Solution()
print(a.summaryRanges([1, 4, 5, 6, 8, 10]))
