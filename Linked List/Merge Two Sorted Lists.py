__author__ = 'drzzh'

'''
类似merge sort后的merge，最后一个list完结以后，直接吧另外一个赋给cur.next比较简单

Time: O(max(m,n))
Space: O(1)

'''


class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

c = ListNode(1)
prev = c
for i in range(4):
    prev.next = ListNode(i+2)
    prev = prev.next

b = ListNode(1)
prev = b
for i in range(3):
    prev.next = ListNode(i+2)
    prev = prev.next


def printList(head):
    cur = head
    while cur:
        if cur.next:
            print("%d -> " % cur.val)
        else:
            print(cur.val)
        cur = cur.next


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        p1 = l1
        p2 = l2
        new = ListNode(-1)
        cur = new
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        left = p1 if  p1 else p2
        cur.next = left
        return new.next

printList(c)
printList(b)
a = Solution()
printList(a.mergeTwoLists(c,c))