__author__ = 'drzzh'

'''
    ()(()(): 如果pop一次stack不为空，就index-stack.top()
    ())()(): 引入start， ）后面start更新

    Time: O(n)
    Space: O(n)

'''


class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        result = 0
        stack = []
        start = -1
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        result = max(index - stack[-1], result)
                    else:
                        result = max(index - start, result)
                else:
                    start = index
        return result
