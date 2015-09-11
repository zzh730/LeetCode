__author__ = 'drzzh'


'''
    很简单的dfs， 注意sum可能是负的

'''

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        self.result = []
        if not root:
            return []
        self.dfs(root, sum, [])
        return self.result

    def dfs(self, cur, s, lst):

        if not cur.right and not cur.left:
            if s - cur.val == 0:
                lst.append(cur.val)
                self.result.append(lst)
            return
        else:
            if cur.left:
                self.dfs(cur.left, s - cur.val, lst + [cur.val])
            if cur.right:
                self.dfs(cur.right, s - cur.val, lst + [cur.val])
