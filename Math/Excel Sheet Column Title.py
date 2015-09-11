__author__ = 'drzzh'

'''
    10进制转化26进制， 26可以替换成任何进制，
    tricky part： 去余为0时，可以每次-1来使结果映射在0-25，对应1-26个字母

'''

class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        result = ''
        while n > 0:
            n -= 1
            result = chr(n % 26 + 65) + result
            n = n / 26

        return result


a = Solution()

