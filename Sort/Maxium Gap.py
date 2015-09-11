__author__ = 'drzzh'
from math import log


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        if not nums:
            return 0
        maxlen = int(log(max(nums), 10)) + 1
        nums = self.radix(nums, maxlen)
        gap = 0
        for i in range(1, len(nums)):
            gap = nums[i] - nums[i - 1] if nums[i] - nums[i - 1] > gap else gap
        return gap

    # java直接翻译过来的，效率很差
    def radixsort(self, nums):
        largest = max(nums)
        radix = 1
        for i in range(int(log(largest, 10)) + 1):
            count = dict(zip([i for i in range(11)], [0] * 11))
            temp = [0] * len(nums)
            for j in nums:
                count[int(j / radix) % 10 + 1] += 1  # 对实际要算的数+1， 这样前一个数的个数，就是这个数的坐标
            for j in range(1, len(count)):
                count[j] += count[j - 1]
            for j in nums:
                temp[count[int(j / radix) % 10]] = j
                count[int(j / radix) % 10] += 1
            for j in range(len(temp)):
                nums[j] = temp[j]
            radix *= 10
        return nums

    #python版，效率好很多
    def radix(self, nums, maxlen):
        for i in range(maxlen):
            temp = [[] for i in range(10)]
            for k in nums:
                temp[int(k / 10 ** i) % 10].append(k)
            nums = []
            for lst in temp:
                nums.extend(lst)
        return nums


a = Solution()
print(a.maximumGap([100, 3, 2, 1]))
