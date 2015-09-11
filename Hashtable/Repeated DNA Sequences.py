__author__ = 'drzzh'
'''
    result用set比较好, 不存在重复元素作为结果

'''


class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        table = set()
        result = set()
        n = len(s)
        if n == 10:
            return []
        for index in range(n - 9):
            if s[index:index + 10] in table:
                result.add(s[index:index + 10])
            else:
                table.add(s[index:index + 10])
        return list(result)


a = Solution()

print(a.findRepeatedDnaSequences("AAAAAAAAAAA"))
