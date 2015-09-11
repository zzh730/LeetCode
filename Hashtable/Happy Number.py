__author__ = 'drzzh'

"""
    用set存每个中间结果就行，遇到重复的结束
"""

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        temp = set()
        num = n
        while num not in temp:
            temp.add(num)
            num = self.bit(num)
            if num == 1:
                return True
        return False

    def bit(self, n):
        num = []
        if n < 10:
            return n * n
        while n >= 10:
            num.append(n % 10)
            n = int(n / 10)
        else:
            num.append(n)
        result = 0
        for item in num:
            result += item * item
        return result


a = Solution()
print(a.isHappy(3))