__author__ = 'drzzh'

'''
        思想是递归的求


'''


class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        if n < 10:
            return 1
        base = 10 ** (len(str(n)) - 1)
        answer = int(n / base)
        return self.countDigitOne(base - 1) * answer + ((n - base + 1) if answer == 1 else base) + self.countDigitOne(
            n % base)
