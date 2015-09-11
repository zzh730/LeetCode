__author__ = 'drzzh'

'''
    GREEDY的应用， 实现用了好长时间，代码又丑又臭， copy了别人的
    对index的实现很巧妙， i <= prev, i++, 这样就一直增长，保持在n内
    cur代表当前最大能到达的index
'''


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def jump(self, nums):
        n = len(nums)
        i, res = 0, 0
        cur, prev = 0, 0
        while cur < n - 1:
            while i <= prev:
                cur = max(cur, i + nums[i])
                i += 1
            if prev == cur:
                return -1
            prev = cur
            res += 1
        return res
