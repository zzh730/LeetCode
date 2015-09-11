__author__ = 'drzzh'
"""
一到常规dp，
    重要的是如何理解最大连续子串和
        1.temp = 当前数字+temp
            如果当前数字还比temp大，说明可以重新开始计算temp， 所以temp = 当前数字
            否则继续加
        2.每次对temp操作后都要和max比，所以把比较留在最外边

    time: O(n)
    space: O(1)

"""

def maxSubArray(A):
    cur = A[0]
    result = A[0]
    if A == []:
        return 0
    for item in A[1:]:
        cur += item
        if item >= cur:
            cur = item
        result = max(result, cur)
    return result


A = [0,3,-1]
print(maxSubArray(A))

