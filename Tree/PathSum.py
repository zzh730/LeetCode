__author__ = 'drzzh'

'''
看好base case

'''


def hasPathSum(self, root, sum):
    if not root:
        return False
    if sum == root.val and root.left == None and root.right == None:
        return True
    else:
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)