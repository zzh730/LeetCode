__author__ = 'drzzh'

'''
    如果用切片回memory limited exceed
    这个方法巧妙在每次先从postorder里pop root，然后先构建右子树，这样postorder就不用切片，
    每次自然就减小了

'''


class TreeNode:
    pass


class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return
        root = TreeNode(postorder.pop())
        if len(inorder) == 1:
            return root
        rootIndex = inorder.index(root.val)
        root.right = self.buildTree(inorder[rootIndex + 1:], postorder)
        root.left = self.buildTree(inorder[:rootIndex], postorder)

        return root
