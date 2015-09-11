__author__ = 'drzzh'
"""
once you realize that the output is a fibbanaqi sequence
it is obvious to solve it.
"""


def climbStairs(n):
    f = [1, 2]
    if n < 3:
        return n
    else:
        for i in range(2, n):
            f.append(f[i - 2] + f[i - 1])
        return f.pop()


print(climbStairs(0))