__author__ = 'drzzh'

'''
二分查找的题,注意的是如果是分数，返回时的条件是：  mid*mid <= x and (mid+1)*(mid+1) > x

Time: O(logn)
'''


class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x < 0:
            return -1
        if not x:
            return 0
        if x ==1:
            return 1
        left = 1
        right = int(x/2)
        while left <= right + 1:
            mid = int((left+right)/2)
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid
            elif mid*mid > x:
                right = mid-1
            else:
                left = mid+1