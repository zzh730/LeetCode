__author__ = 'drzzh'

'''
    思想是从左到右，从右到左扫两次数组，分别记录乘积，然后相乘
    无需乘法

'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        res = [1]
        for i in nums[:-1]:
            res.append(res[-1] * i)
        right = 1
        n = len(nums)
        for i in range(n):
            res[n - i - 1] *= right
            right *= nums[n - i - 1]
        return res


'''
    如果可以用除法！！！
    特殊case：
        （0，0）——》（0，0）
        （0，1）——》（1，0）
        当有一个0时，应该记录除了零以外的积，赋给0
        有多个0时，就无需担心
'''


class Solution1:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        def product(nums):
            res = 1
            addition = 1
            count = 1
            for i in nums:
                if not i and count:
                    res = 0
                    count -= 1
                    continue
                res *= i
                addition *= i
            return res, addition

        res, addition = product(nums)
        for index, i in enumerate(nums):
            if i:
                nums[index] = int(res / i)
            else:
                nums[index] = addition
        return nums
