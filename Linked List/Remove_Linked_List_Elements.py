__author__ = 'drzzh'

"""
只需要用个fake Head 就能避免corner case

"""




class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

def printList(head):
    cur = head
    while cur:
        if cur.next:
            print("%d -> " % cur.val)
        else:
            print(cur.val)
        cur = cur.next


class Solution:
    def removeElements(self,head,val):
        fakeHead = ListNode(-1)
        fakeHead.next = head
        pre = fakeHead
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return fakeHead.next
