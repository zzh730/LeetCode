__author__ = 'drzzh'

from collections import deque

'''
    本质还是考level order的遍历，用一个队列，一个stack实现就好
'''


class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if not root:
            return []
        stack1 = deque([root])
        stack2 = []
        count1 = 1
        count2 = 0
        result = []
        while stack1:
            cur = stack1.popleft()
            count1 -= 1
            if cur.left:
                stack2.append(cur.left)
                count2 += 1
            if cur.right:
                stack2.append(cur.right)
                count2 += 1
            if count1 == 0:
                count1 = count2
                result.append(stack2)
                stack1.extend(stack2)
                stack2 = []
                count2 = 0
        lst = [root.val]
        for index, item in enumerate(result):
            if item:
                lst.append(item[-1].val)
        return lst
