__author__ = 'drzzh'

'''
    1. 先交换保证m > n
    2. shift保证是1（前提是s,t长度只差1),有一个不一样，count+1
'''
class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):
        m = len(s)
        n = len(t)
        if n > m:
            return self.isOneEditDistance(t, s)
        if m - n > 1:
            return False
        if max(m, n) == 1 and min(m, n) == 0:
            return True
        count = 0
        shift = 0
        if m - n == 1:
            shift = 1
        for i in range(m):
            temp = t[i - shift * count] if i - shift * count < n else None
            if s[i] != temp:
                count += 1
        return count == 1
