__author__ = 'drzzh'

"""
preorder里第一个就是root， 在inorder找到root坐标，左边就是root左子树，右边就是右子树

    提取inorder的元素，使其按照preorder里的顺序排列，然后这个sublist当成preorder，recursive遍历

    time:O(nlog^2n)
    space:O(nlogn)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    if not preorder:
        return None

    cur = preorder.pop(0)
    node = TreeNode(cur)

    left = inorder[:inorder.index(cur)]
    right = inorder[inorder.index(cur) + 1:]
    if left:
        sort = [preorder.index(i) for i in left]
        sort.sort()
        preleft = [preorder[i] for i in sort]
        node.left = buildTree(preleft, left)
    if right:
        sort = [preorder.index(i) for i in right]
        sort.sort()
        preright = [preorder[i] for i in sort]
        node.right = buildTree(preright, right)
    return node


"""
据说当左子树构建好了以后，preorder就只剩下右子树的了，所以不用切分preorder，

time: O(nlogn)
space:O(nlogn)


"""


def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    rootValue = preorder.pop(0)
    root = TreeNode(rootValue)
    inorderIndex = inorder.index(rootValue)

    root.left = buildTree(preorder, inorder[:inorderIndex])
    root.right = buildTree(preorder, inorder[inorderIndex + 1:])

    return root

