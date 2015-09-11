__author__ = 'drzzh'

'''
看到有序数组直接想到二分查找，用递归，每次就先求root，然后递归去接left和right

Time:O(n)
Space:O()

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
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        head = 0
        tail = len(num) - 1
        index = int((head + tail) / 2)
        root = TreeNode(num[index])
        root.left = self.sortedArrayToBST(num[:index])
        root.right = self.sortedArrayToBST(num[index + 1:])
        return root


def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val)
    printTree(root.right)


printTree(tree)
a = Solution()
root = a.sortedArrayToBST([1, 2, 3, 4, 5])

printTree(root)