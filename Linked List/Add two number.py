__author__ = 'drzzh'




"""
别忘了carry
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

def construct(value):
    head = ListNode(value[0])
    cur = head
    for i in range(1,len(value)):
        cur.next = ListNode(value[i])
        cur = cur.next
    return head


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        cur = ListNode(0)
        head = cur
        carry = 0
        cur1 = l1
        cur2 = l2
        while cur1 and cur2:
            num = cur1.val + cur2.val + carry
            carry = 0
            if num > 9:
                carry = 1
                num = num % 10
            cur.next = ListNode(num)
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next
        cur1 = cur1 if cur1 else cur2
        while cur1:
            num = cur1.val + carry
            carry = 0
            if num > 9:
                carry = 1
                num = num % 10
            cur.next = ListNode(num)
            cur = cur.next
            cur1 = cur1.next
        if carry:
            cur.next = ListNode(carry)
        return head.next




heada = construct([0])
headb = construct([0])

a = Solution()
printList(a.addTwoNumbers(heada,headb))


