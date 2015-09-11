__author__ = 'drzzh'

"""
题目不难， 主要是中间如何判断循环的结束，还有什么时候把char加入prefix

思路是取最长的单词遍历每个字母，对这个字母遍历所有字符喘

Time: O(nL)

"""
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        prefix = ""
        if not strs:
            return ""
        word = strs[0]
        for string in strs:
            if len(string) > len(word):
                word = string
        for index, char in enumerate(word):
            stop = False
            for count, string in enumerate(strs):
                if index > len(string) - 1:
                    stop = True
                    break

                elif index <= len(string) - 1 and char != string[index]:
                    stop = True
                    break
                if not stop and count == len(strs) - 1:
                    prefix += char
            if stop:
                break
        return prefix


a = Solution()
strs = ['a', 'a']
print(a.longestCommonPrefix(strs))