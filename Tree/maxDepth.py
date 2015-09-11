__author__ = 'drzzh'

"""
很简单的递归，主要是在类里递归要加上self
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


tree = TreeNode(0)
tree.left = TreeNode(1)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)

class solution:
    def maxDepth(self, root):
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1