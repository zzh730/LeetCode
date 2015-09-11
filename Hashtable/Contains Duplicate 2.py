__author__ = 'drzzh'

from collections import deque

"""
    用一个窗口存k个数,用双端队列实现,
    用一个dic存k个已读取的数

    Time: O(n)
    Space: O(k)
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) < 2:
            return False
        queue = deque([])
        dic = {}
        for num in nums:
            if len(queue) <= k:
                if num in dic:
                    return True
                else:
                    dic[num] = 1
                queue.append(num)
            else:
                key = queue.popleft()
                del dic[key]
                if num in dic:
                    return True
                else:
                    queue.append(num)
                    dic[num] = 1
        return False
