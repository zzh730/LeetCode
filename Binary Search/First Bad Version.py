__author__ = 'drzzh'


'''
    很简单的题，判断mid的时候再判断一下mid - 1就行

    Time: O(lgn)

'''
def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, n
        while a <= b:
            mid = int((a + b) / 2)
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                b = mid - 1
            else:
                a = mid + 1
        return a
