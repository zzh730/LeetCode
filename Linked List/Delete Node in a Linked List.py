__author__ = 'drzzh'

'''
    思路就是复制下一个节点的值，然后删最后一个节点
'''

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        cur = node
        while cur.next:
            cur.val = cur.next.val
            if cur.next.next:
                cur = cur.next
            else:
                break
        cur.next = None