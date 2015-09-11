__author__ = 'drzzh'
"""
key idea is to reverse the whole string then reverse the word
"""
class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        a = 0
        for i in range(len(s)):
            if s[i] == ' ':
                s[a:i] = reversed(s[a:i])
                a = i+1
            elif i == len(s) - 1:
                s[a:i+1] = reversed(s[a:i+1])
        s.reverse()
