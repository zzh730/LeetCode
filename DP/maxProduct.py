__author__ = 'drzzh'


"""
DP问题： 重点是要有n-1的最小负数
        可以用一个min一个max来维护

        maxnum = max(item, maxpre * item, minpre * item)
        minnum = min(item, maxpre * item, minpre * item)

    time：O(n)
    space: O(1)

"""

def maxProduct(A):
    if A ==[]:
        return 0
    result = A[0]
    maxnum = A[0]
    minnum = A[0]
    for item in A[1:]:
        maxpre = maxnum
        minpre = minnum
        maxnum = max(item, maxpre * item, minpre * item)
        minnum = min(item, maxpre * item, minpre * item)
        result = max(result, maxnum)

    return result


A = [0,-4,-1]
print(maxProduct(A))


