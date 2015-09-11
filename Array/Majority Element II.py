__author__ = 'drzzh'

'''
    Boyer-Moore algorithm:
        如果数组有个元素个数超过n/2，可以Time: O(n) Space: O(1)找出
        方法是：
            1. count = 0，candidate = 0
            2. 扫数组，n!= candidate count--，如果count = 0， 就candidate = n
            3. 思想就是就算主元素的count为零了，剩下的数组里主元素还是比其他元素多，所以candidate一定是主元素
    这道题是n/3, 可能出现俩元素，所以设两个candidate
    注意实现时的elif，不能多加if
'''


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        c1, c2, count1, count2 = None, None, 0, 0
        for n in nums:
            if n == c1:
                count1 += 1
            elif n == c2:
                count2 += 1
            elif count2 == 0:
                c2, count2 = n, 1
            elif count1 == 0:
                c1, count1 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        return list(c for c in (c1, c2) if nums.count(c) > len(nums) / 3)
