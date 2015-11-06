"""
    思路很直接, 就是用hashtable判重,
    注意: 1. pattern字数和str的word字数应该一致,要不直接false
         2. 每个key存的值也不能相同
    Time: O(KM)
    Space: O(max(K, M))
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        words = str.strip().split()
        if len(words) != len(pattern):
            return False
        dic = {}
        for index, i in enumerate(pattern):
            if i not in dic:
                if words[index] not in dic.values():
                    dic[i] = words[index]
                else:
                    return False
            else:
                if words[index] != dic[i]:
                    return False
        return True


a = Solution()
str = "cat dog dog boy"
print(a.wordPattern("abba", str))
print("abba")
