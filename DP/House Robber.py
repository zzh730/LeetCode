__author__ = 'drzzh'
'''
一道线性DP，主要不同的是对于每一步需要遍历之前的解才行 0 ~ index - 2

Time: O(n^2)
Space: O(n)
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        table = []
        if not num:
            return 0
        if len(num) == 1:
            return num[0]
        table.append(num[0])
        if len(num) == 2:
            return max(num[0], num[1])
        table.append(max(num[0], num[1]))
        result = max(table)
        for index in range(2, len(num)):
            temp = 0
            for i in range(index - 1):
                temp = max(table[i], temp)
            temp += num[index]
            table.append(temp)
            result = max(result, temp)
        return result


a = Solution()
print(a.rob([1, 3, 1]))


'''
更牛逼的解法，每个房子分两种情况：
    1.包含，total - prev + this
    2.不包含, total

'''