__author__ = 'drzzh'


"""
    思路是取[2,sqrt(n)+1]之间的数，把他们的倍数都mark，不在标记的数就是质数
    trick： 2 - sqrt（n）+ 1，避免重复计算， 如果p*q = n p是质数, 无需计算q*p
    trick: 标记p的倍数时，直接从p*p开始，步长为p(都为p倍数，无需step=1)
    python：不能用dictionary，会memory limited exceed

    Time: O(nloglonn)
    Space: O(n)
"""


import math
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        dic = [True] * n
        dic[0] = False
        dic[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if dic[i]:
                for j in range(i * i, n, i):
                    dic[j] = False
        return sum(dic)