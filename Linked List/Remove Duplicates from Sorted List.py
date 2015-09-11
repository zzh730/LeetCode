__author__ = 'drzzh'




# Definition for singly-linked list.
class ListNode:
    pass
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        if not head:
            return None
        if not head.next:
            return head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head