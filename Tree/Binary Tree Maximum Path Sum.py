__author__ = 'drzzh'

'''
    每个节点总共有四种情况：
        1. only node
        2. left+node
        3. right+node
        4. left+right+node
    用一个属性记录最大值，每次返回第1，2，3给父节点
'''


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        if not root:
            return 0
        self.res = root.val
        self.maxSum(root)
        return self.res

    def maxSum(self, cur):
        if not cur:
            return 0
        left = self.maxSum(cur.left)
        right = self.maxSum(cur.right)
        single = max(cur.val, cur.val + max(left, right))
        self.res = max(self.res, left + right + cur.val, single)
        return single
