__author__ = 'drzzh'

'''
    这题思路是

'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        fake = ListNode(-1)
        fake.next = head
        p1, p2 = fake, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        second = p1.next
        p1.next = None
        second = self.reverse(second)
        cur1 = head
        while cur1 and second:
            temp1 = cur1.next
            temp2 = second.next
            cur1.next = second
            second.next = temp1
            if temp1:
                cur1 = temp1
            else:
                cur1 = cur1.next
            second = temp2
        return

    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
