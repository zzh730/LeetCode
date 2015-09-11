__author__ = 'drzzh'

'''
    2的平方意味着二进制里只有一个1， 直接n & n - 1

'''


class Solution:
    def isPowerOfTwo(self, n):
        return (n > 0) and not n & (n - 1)
