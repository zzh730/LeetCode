__author__ = 'drzzh'

"""
用一个栈的时候需要再来俩变量存下一行节点数count1和当前行节点数count2
    time:O(n)
    space:O(n)

"""

from collections import deque
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


def levelorder(root):
    queue = deque([root])
    stack2, result = [], []
    count1 = 0
    count2 = 1
    if not root:
        return result
    while (queue):
        p = queue.popleft()
        count2 -= 1
        stack2.append(p.val)
        if p.left:
            queue.append(p.left)
            count1 += 1
        if p.right:
            queue.append(p.right)
            count1 += 1
        if count2 == 0:
            result.append(stack2)
            stack2 = []
            count2 = count1
            count1 = 0
    return result


tree1 = TreeNode(0)
print(levelorder(tree))
