__author__ = 'drzzh'



'''
    与第一个不一样在于去了（），加上了*/
    想要不超时对于*/直接第一遍遍历就直接算，
        由于/的出现，得正序扫描，10000/9/10这样的例子，逆序回有0作为被除数
        因为是正序扫，做减法的时候很麻烦，所以第二遍的时候把俩栈逆序
        getNext一定要返回j的值，用它来跟新i

    Time: O(n)
    Space: O(n)

'''

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s = s.strip()
        stack1 = []
        stack2 = []
        i = 0

        def getNext(s, i):
            j = i + 1
            while j < len(s):
                if s[j] not in "0123456789":
                    break
                j += 1
            return j - 1, int(s[i:j])

        while i < len(s):
            if s[i] in "0123456789":
                i, temp = getNext(s, i)
                stack1.append(temp)
            elif s[i] in "*/":
                num1 = stack1.pop()
                j, num2 = getNext(s, i + 1)
                if s[i] == "*":
                    stack1.append(num1 * num2)
                else:
                    stack1.append(int(num1 / num2))
                i = j
            elif s[i] in "+-":
                stack2.append(s[i])
            i += 1
        stack1.reverse()
        stack2.reverse()
        while stack2:
            if stack2.pop() == "+":
                stack1.append(stack1.pop() + stack1.pop())
            else:
                stack1.append(stack1.pop() - stack1.pop())
        return stack1[0]
