__author__ = 'drzzh'

"""
用异或，单个数字会成最后的结果,python里是^
Time: O(n)
Space: O(1)
"""


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = A[0]
        for cur in A[1:]:
            result ^= cur
        return result