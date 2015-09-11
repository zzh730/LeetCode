__author__ = 'drzzh'

"""
都是非递归写法：
    1。backtracking 如果左节点存在，入栈，访问，不存在，出栈，访问右节点，注意终止条件，stack空了要停止循环
    2. 根节点出栈，然后如果有右节点就入栈，如果有左节点就入栈
    3. 一定注意在else后检查stack是否为空

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


def preorder(root):
    if root == None:
        return 0
    p = root
    stack = []
    while (p != None or stack != None):
        if p:
            print(p.val)
            stack.append(p)
            p = p.left
        else:
            if not stack:
                break
            p = stack.pop().right


def preorder1(root):
    if root == None:
        return 0
    p = root
    stack = [root]
    while (stack):
        p = stack.pop()
        print(p.val)
        if p.right:
            stack.append(p.right)
        if p.left:
            stack.append(p.left)
