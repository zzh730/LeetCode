__author__ = 'drzzh'


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dic1 = {}
        for char in s:
            if char not in dic1:
                dic1[char] = 1
            else:
                dic1[char] += 1
        for char in t:
            if char not in dic1:
                return False
            else:
                dic1[char] -= 1
            if dic1[char] < 0:
                return False
        return True


a = Solution()
print(a.isAnagram("nagaram", "anagram"))
