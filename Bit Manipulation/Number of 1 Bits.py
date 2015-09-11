__author__ = 'drzzh'

'''
    and可对10进制进行操作，效果与2进制一样
        n = 6
        110 & 101 = 100
        count = 1
        n = 4
        100 & 011 = 0
        count = 2
    算法每次移除一个1


'''
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count


a = Solution()
print(a.hammingWeight(5))
