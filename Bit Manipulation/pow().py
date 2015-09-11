__author__ = 'drzzh'
'''
也算是二分查找的应用吧，思想是：
    递归求x的n/2次方，然后相乘即可，
注意的是：
       1.base case: n = 1 返回x
       2.n%2不等于0，如果 n<0 要补上 1/x
       3.计算n/2时，要int(float(n)/2),否则会无限循环栈



'''


class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        y = self.pow(x, int(float(n) / 2))
        if n % 2 == 0:
            return int(y * y)
        else:
            return int(y * y * (x if n > 0 else 1 / x))


a = Solution()
print(a.pow(0.1, -1))