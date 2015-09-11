__author__ = 'drzzh'

'''
一个recursion解决问题，主要是求树的深度，
    如果两边都平衡了，那么此节点平衡的条件是左右子树高度差小于等于1

    或者设定flag=true，一旦不平衡直接返回树高0，flag就一直会是false

'''
fact = True

def isBalanced(root):
    if not root:
        return True
    fact = True
    depthf(root)
    return fact


def depthf( root, fact):
    if not root or not fact:
        return 0
    else:
        left = depthf(root.left)
        if not fact:
            return 0
        right = depthf(root.right)
        if not fact:
            return 0
        diff = left - right
        if diff > 1 or diff < -1:
            fact = False
        return max(left, right) + 1
'''
直接算树高 不平衡返回-1
'''


class Solution1:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return True
        return False if self.isB(root) == -1 else True


    def isB(self, root):
        if not root:
            return 0
        left = self.isB(root.left)
        right = self.isB(root.right)
        if left >= 0 and right >= 0:
            if -2<left - right < 2:
                return max(left,right) + 1
        return -1