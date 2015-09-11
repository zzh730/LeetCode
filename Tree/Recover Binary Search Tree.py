__author__ = 'drzzh'
'''
想了半天出了一种space:O(n)的方法，代码太长太臭就舍弃了

参考了huntfor的博客，特别简洁，用中序遍历，只储存前驱，
    第一次出错的地方一定是：prev是第一个错误节点，cur在其后，因为prev > prev of prev, prev > cur, SO first = prev
    第二次出错在于，prev > cur, SO second = cur

原文地址：http://huntfor.iteye.com/blog/2077665

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


tree = TreeNode(4)
tree.right = TreeNode(2)
tree.right.right = TreeNode(1)
'''
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(4)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(8)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(6)
tree.right.left.left = TreeNode(9)
tree.right.left.right = TreeNode(10)
'''


class Solution:
    # @param root, a tree node
    # @return nothing, modify the binary tree in-place instead.
    def recoverTree(self, root):
        self.first,self.second,self.prev = None,None,None
        self.inorder(root)
        self.swap()
        return root

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.prev and root.val < self.prev.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.inorder(root.right)

    def swap(self):
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp


def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val)
    printTree(root.right)


printTree(tree)
a = Solution()
root = a.recoverTree(tree)

printTree(root)

