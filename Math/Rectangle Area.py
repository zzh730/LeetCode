__author__ = 'drzzh'

'''
    第一个是自己做的又丑又笨的方法, 对每种边界条件都进行判断,其丑无比
    第二个是大牛写的, 很简单, 不重合之间返回面积和, 重合减去重合面积,
        重合面积怎么算, 夹逼, 小的里取大的,大的里要小的.

'''


class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        leftUp = (C, D)
        leftDown = (A, B)
        rightUp = (G, H)
        rightDown = (E, F)
        areaBoth = self.area(leftDown, leftUp) + self.area(rightDown, rightUp)
        if G < C:
            leftUp, rightUp = self.switch(leftUp, rightUp)
            leftDown, rightDown = self.switch(leftDown, rightDown)
        if leftUp[0] <= rightDown[0] or leftDown[1] >= rightUp[1] or rightDown[1] >= leftUp[1]:
            return areaBoth
        if self.within(leftUp, rightDown, rightUp) and self.within(leftDown, rightDown, rightUp):
            return areaBoth - self.area(leftDown, leftUp)
        elif self.within(leftUp, rightDown, rightUp) and not self.within(leftDown, rightDown, rightUp):
            if leftDown[0] < rightDown[0] and leftDown[1] < rightDown[1]:
                return areaBoth - self.area(rightDown, leftUp)
            elif leftDown[0] < rightDown[0] and leftDown[1] >= rightDown[1]:
                return areaBoth - self.area((rightDown[0], leftDown[1]), leftUp)
            else:
                return areaBoth - self.area((leftDown[0], rightDown[1]), leftUp)
        elif not self.within(leftUp, rightDown, rightUp) and self.within(leftDown, rightDown, rightUp):
            return areaBoth - self.area(leftDown, (leftUp[0], rightUp[1]))
        else:
            if rightDown[1] < leftDown[1] < rightUp[1]:
                return areaBoth - self.area((rightDown[0], leftDown[1]), (leftUp[0], rightUp[1]))
            elif rightDown[0] >= leftDown[0]:
                return areaBoth - self.area(rightDown, (leftUp[0], rightUp[1]))
            elif rightDown[0] < leftDown[0]:
                return areaBoth - self.area((leftDown[0], rightDown[1]), (leftUp[0], rightUp[1]))

    def switch(self, A, B):
        return B, A

    def within(self, a, x, y):
        if x[0] <= a[0] <= y[0] and x[1] <= a[1] <= y[1]:
            return True
        else:
            return False

    def area(self, a, b):
        return (b[0] - a[0]) * (b[1] - a[1])


class Solution2:
    def computeArea(self, A, B, C, D, E, F, G, H):
        left = max(A, E)
        bottom = max(B, F)
        right = min(C, G)
        top = min(D, H)
        union = 0
        if top >= bottom and left <= right:
            union = (top - bottom) * (right - left)
        return (C - A) * (D - B) + (G - E) * (H - F) - union
