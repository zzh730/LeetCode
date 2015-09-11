__author__ = 'drzzh'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        self.invertTree1(root)
        return root

    def invertTree1(self, root):
        if not root:
            return
        if root.left == None and root.right == None:
            return
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree1(root.left)
            self.invertTree1(root.right)
