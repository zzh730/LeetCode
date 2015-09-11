__author__ = 'drzzh'
'''
一个比较愚蠢的递归解法：
    先求左子树的镜像，然后判断镜像树是否和右子树相等
如何求树的镜像：
    递归啊，先交换当前节点的左右子树，然后递归解左右子树的镜像树

'''




class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        left = self.minor(root.left)
        return self.isSameTree(left, root.right)


    def minor(self, root):
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.minor(root.left)
        self.minor(root.right)
        return root


    def isSameTree(self, p, q):
        if not q and not p:
            return True
        if not q or not p:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

'''
更简明的recursive，直接递归的去求left.left && right.right 还有left.right&&right.left
'''

class solution:
    def isSymmetric(self, root):
        return self.symmetric(root,root)
    def symmetric(self,left,right):
        if not right or not left:
            return False
        return left.val == right.val and self.symmetric(left.left,right.right) and self.symmetric(left.right,right.left)
