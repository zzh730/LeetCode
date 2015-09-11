__author__ = 'drzzh'


class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        left = set(["(", "[", "{"])
        for char in s:
            if char in left:
                stack.append(char)
            elif char == ")":
                if not stack:
                    return False
                temp = stack.pop()
                if not temp or temp != "(":
                    return False
            elif char == "]":
                if not stack:
                    return False
                temp = stack.pop()
                if not temp or temp != "[":
                    return False
            elif char == "}":
                if not stack:
                    return False
                temp = stack.pop()
                if not temp or temp != "{":
                    return False
        if not stack:
            return True
        else:
            return False


a = Solution()
print(a.isValid("]"))
