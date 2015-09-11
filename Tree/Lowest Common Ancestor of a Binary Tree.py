__author__ = 'drzzh'


'''
     贼聪明的算法实现，left和right代表pq是否在左右子树， 取值就是（None, p, q）
     如果left right都存在，那root就是lca，
     否则返回存在值的子树

'''

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, q, p):
            return root
        left, right = (self.lowestCommonAncestor(child, p, q) for child in (root.left, root.right))
        return root if left and right else left or right
