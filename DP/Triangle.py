__author__ = 'drzzh'


"""
    dp的应用， 只需存上次loop的计算结果，取左右最小的保存，
    Time: O(n^2)
    Space: O(n)

"""


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        elif len(triangle) < 2:
            return triangle[0][0]
        last = triangle[0]
        for i in range(1, len(triangle)):
            res = []
            for j in range(len(triangle[i])):
                if j == 0:
                    res.append(triangle[i][j] + last[j])
                elif j == len(triangle[i]) - 1:
                    res.append(triangle[i][j] + last[j - 1])
                else:
                    res.append(min(last[j - 1], last[j]) + triangle[i][j])
            last = res
        return min(last)
