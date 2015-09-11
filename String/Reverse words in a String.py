__author__ = 'drzzh'

"""
one pass without split();
Trick is to keep track of when the word starts and ends,
use substring(i,j) to append

Watch out for the base case:
    1)one word
    2)no whitespace in head
    3)last whitespace in the result
"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        a = len(s)-1
        b = 0
        result = ""
        if ' ' not in s:
            return s
        while(a>-1):
            if s[a] != ' ':
                b += 1
            elif s[a] == ' ' and b != 0:
                result += s[a+1:a+b+1] + ' '
                b = 0
            if a == 0 and b != 0:
                result += s[a:a+b+1]
            a-=1
        return result[:-1]#如果第一个字符是0，抵消26行的空格，如果不是，抵消29的空格


a = Solution()
print(a.reverseWords("I am King "))