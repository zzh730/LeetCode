__author__ = 'drzzh'
"""
得用preorder里的backtracking做，区别是先访问左节点在访问根节点

"""


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

stack = []


def inorder(root):
    if root == None:
        return 0
    p = root
    stack = []
    while (p != None or stack != None):
        if p:
            stack.append(p)
            p = p.left
        else:
            if not stack:
                break
            p = stack.pop()
            print(p.val)
            p = p.right
'''
非递归中序遍历


'''

class solution:

    def inorder(self, root):
        stack = []
        if not root:
            return None
        cur = root
        while stack or cur:
            if cur:
                if cur.left:
                    stack.append(cur)
                    cur = cur.left
                else:
                    print(cur.val)
                    cur = cur.right
            else:
                cur = stack.pop()
                print(cur.val)
                cur = cur.right