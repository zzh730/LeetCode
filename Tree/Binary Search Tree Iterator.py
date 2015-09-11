__author__ = 'drzzh'

'''
    迭代避免nonetype的技巧, 把cur放在while里,最后在cur = cur.next
    此题题意是把最小数放在stack里,难点是pop了最小数后,次小数要再pop节点右子树的左子树里去找

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        if root:
            self.stack.append(root)
            cur = root.left
            while cur:
                self.stack.append(cur)
                cur = cur.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if self.stack else False

    # @return an integer, the next smallest number
    def next(self):
        if self.hasNext():
            small = self.stack.pop()
            cur = small
            while cur:
                if cur.left:
                    self.stack.append(cur.left)
                cur = cur.right
            return small.val


root = TreeNode(1)

a = BSTIterator(root)

print(a.next())
