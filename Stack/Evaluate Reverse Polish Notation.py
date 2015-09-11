__author__ = 'drzzh'



class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        operators = "+-*/"
        if not tokens:
            return None
        if len(tokens) == 1:
            return int(tokens[0])
        for item in tokens:
            if item not in operators:
                temp = int(item)
                stack.append(temp)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if item == "+":
                    stack.append(first + second)
                elif item == "-":
                    stack.append(first - second)
                elif item == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(first*1.0 / second))
        return stack.pop()

a = Solution()
print(a.evalRPN(["4","13","5","/","+"]))
