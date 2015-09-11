__author__ = 'drzzh'


"""
如果最后一个字符是空格得把空格去了在计算

"""

class Solution:
    # @return a string
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        index = len(s) - 1
        if not s or s[index] == ' ' or '':
            return 0
        count = 0
        while index > -1 and s[index] != ' ':
            count += 1
            index -= 1
        return count