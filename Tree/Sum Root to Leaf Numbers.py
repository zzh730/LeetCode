__author__ = 'drzzh'

"""

"""


def sumNumbers(root):
    if root == None:
        return 0
    path = 0
    result = 0
    result = pathSum(root, path,result)
    return result


def pathSum(root, path,result):
    path = path * 10 + root.val
    if not root.left and not root.right:
        result += path
        return result
    else:
        if root.left:
            pathSum(root.left, path)
        if root.right:
            pathSum(root.right, path)