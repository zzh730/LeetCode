__author__ = 'drzzh'

"""
    思路很简单的一道题，唯一的难点在于k,length的关系，k其实应该是k mod Length的值
    中间用mid fakehead tail三个变量记录链表的修改之处
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        if not head:
            return None
        k = k % length
        if min(k,length) == 0:
            return head
        cur = head
        fakeHead = ListNode(-1)
        fakeHead.next = head
        count = 0
        while cur:
            count += 1
            if length - k == count:
                mid = cur
            if not cur.next:
                tail = cur
            cur = cur.next
        fakeHead.next = mid.next
        mid.next = None
        tail.next = head
        return fakeHead.next