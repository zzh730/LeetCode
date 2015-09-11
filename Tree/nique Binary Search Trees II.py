__author__ = 'drzzh'

'''
    DP思路很简单，就是对每个数遍历，然后分左右区间，每个区间产生子树，然后合并
    实现的时候遇到了问题，


    参考另外一种实现方法，自底向上构建树，先构建左右子树可能的列表，然后从列表里遍历构建root，添加进list然后返回。
'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        return self.dfs(1, n)

    def dfs(self, left, right):

        if left > right:
            return [None]
        if left == right:
            return [TreeNode(left)]
        result = []
        for k in range(left, right + 1):
            ltree = self.dfs(left, k - 1)
            rtree = self.dfs(k + 1, right)
            for i in ltree:
                for j in rtree:
                    temp = TreeNode(k)
                    temp.left = i
                    temp.right = j
                    result.append(temp)
        return result


def printTree(root):
    if not root:
        return
    print("left")
    printTree(root.left)
    print("root")
    print(root.val)
    print("right")
    printTree(root.right)


a = Solution()
lst = a.generateTrees(3)
for l in lst:
    printTree(l)
    print("-----")
