__author__ = 'drzzh'

'''
除法就是被除数包含几个除数的问题，但是一个一个去减除数太慢了，所以得扩大除数，通过左移除数到最接近被除数的一个以2为底的基

Time: O(logn)

example:    20 / 2
        operation       result(base)    left
        20 - 2          +1              18
        18 - 4          +2              14
        14 - 8          +4              6
        6 - 4           +2              2
        2 - 2           +1              0
        result    =     10


'''



class Solution():
    # @return an integer
    def divide(self, dividend, divisor):
        isNegetive = ((dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0))
        dividend = abs(dividend)
        divisor = abs(divisor)
        left = dividend
        result = 0
        div = divisor
        base = 1
        while left >= divisor:
            if left >= div:
                left = left - div
                result += base
                div = div << 1
                base = base << 1

            else:
                div = div >> 1
                base = base >> 1
        if isNegetive:
            result = -result
        return min(2147483647, max(-2147483648, result))
