__author__ = 'drzzh'

'''
    负数直接判false
'''


class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        if not s:
            return False
        p1 = 0
        p2 = len(s) - 1
        if p1 == p2:
            return True
        while p1 <= p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
