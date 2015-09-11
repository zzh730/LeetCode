__author__ = 'drzzh'

'''

两种解法：
1.左子树的范围不超过（min,root.val）,右子树不超过（root.val, max）


'''


class Solution():

    def isValidBST(self, root):
        return self.isBST(root, -99999, 99999)


    def isBST(self, root, min, max):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False
        else:
            return self.isBST(root.left, min, root.val) and self.isBST(root.right, root.val, max)


    def isValidBST2(self, root):
        self.prev = -999999999999
        return self.isBST2(root)


    def isBST2(self, root):
        if not root:
            return True
        if self.isBST2(root.left):
            if root.val > self.prev:
                self.prev = root.val
                return self.isBST2(root.right)
        return False