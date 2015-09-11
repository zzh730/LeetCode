__author__ = 'drzzh'

'''
    python占便宜的一种方式
'''


class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))


'''
    面试碰到应该用如下方法：小学乘法的实现
        Three Functions:
            1.multiplyChar(string, char, numOfZeros):return the product of string1 and a char in string2, add zeros accord-
              ing to the position of the char in string2.
            2.addTwoNumbers(lastResult, newResult): accumulate the products of string1 * each char in string2.
            3.main function: return result.

'''
