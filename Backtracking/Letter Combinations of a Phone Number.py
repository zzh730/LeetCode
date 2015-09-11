__author__ = 'drzzh'

import functools

'''
    backtracking其实就是dfs的一种, 遇到就先想怎么用递归的方法解,然后用非递归的方法优化空间
'''


class Solution:
    # @param {string} digits
    # @return {string[]}

    result = []
    dic = {"1": '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', \
           '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}

    def letterCombinations(self, digits):
        self.result = []  # oj重复调用时,需要清除上次的结果
        if not digits:
            return []
        if len(digits) == 1:
            return [x for x in self.dic[digits[0]]]
        self.dfs(0, "", "", digits)
        return self.result

    def dfs(self, index, char, word, digits):
        if index == len(digits):
            self.result.append(word + char)
            return
        else:
            word += char
            for item in self.dic[digits[index]]:
                self.dfs(index + 1, item, word, digits)


"""
    方法2, python reduce函数,用于穷举举时很有用.

"""


class Solution2:
    # @param {string} digits
    # @return {string[]}
    dic = {"1": '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', \
           '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}

    def letterCombinations(self, digits):
        if len(digits) == 1:
            return list((x for x in self.dic[digits]))
        elif not digits:
            return []
        return list(functools.reduce(self.mapper, list(digits)))

    def mapper(self, a, b):
        if len(a) == 1:
            a = [i for i in self.dic[a]]
        b = [i for i in self.dic[b]]
        return [x + y for x in a for y in b]


a = Solution2()
print(a.letterCombinations("22"))
