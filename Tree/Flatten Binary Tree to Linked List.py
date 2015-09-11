__author__ = 'drzzh'
'''
中序遍历，先把右树移到左树下，然后把左树翻转到右树

Time:O(n)
Space:O(n)

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(4)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(8)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(6)
tree.right.left.left = TreeNode(9)
tree.right.left.right = TreeNode(10)


def printtree(root):
    if not root:
        return
    printtree(root.left)
    print(root.val)
    printtree(root.right)


class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return None
        cur = root
        last = root
        stack = []
        while cur or stack:
            if cur:
                if cur.left:
                    stack.append(cur)
                    last = cur                      #record the node that right child should attach
                    cur = cur.left
                else:
                    last = cur                      #easy to forget about this case
                    last.left = cur.right
                    cur.right = None
                    cur = last.left
            else:
                temp = stack.pop()
                last.left = temp.right
                temp.right = None
                cur = last.left
        self.leftToRight(root)
        return root

    def leftToRight(self, root):
        while root:
            root.right = root.left
            root.left = None
            root = root.right


a = Solution()
root = a.flatten(tree)

printtree(root)
