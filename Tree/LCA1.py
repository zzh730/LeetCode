__author__ = 'drzzh'

'''
最低公共祖先的问题，不是BST，没有父节点
    1.top-down recursive：
        1. 如果p,q都在left tree，lca也在left tree，right tree同理
        2. 如果一左一右， 那么这个节点就是lca
        Time:O(n^2)
        Space:it depends

    2.

'''


def LCA(root, p, q):
    if not root:
        return None
    if hasNode(root.left, p) and hasNode(root.left, q):
        return LCA(root.left, q, p)
    if hasNode(root.right, p) and hasNode(root.right, q):
        return LCA(root.right, p, q)
    return root


def hasNode(root, node):
    if not root:
        return False
    if root == node:
        return True
    return hasNode(root.left, node) or hasNode(root.right, node)
