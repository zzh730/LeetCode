__author__ = 'drzzh'

"""
    把所有单词映射成aabbcc这样字典序的模式，然后比较相同就是一个模式


    Time: O(n)
    Space: O(1)
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        sNew = self.process(s)
        tNew = self.process(t)
        return True if sNew == tNew else False


    def process(self, word):
        new = ''
        charlist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
        dic = {}
        index = 0
        for char in word:
            if char not in dic:
                dic[char] = charlist[index]
                index += 1
            new += dic[char]
        return new