__author__ = 'drzzh'


'''
第一种方法比较笨，扫两遍，知道length以后，在legnth-n处停下，删除下一个节点
第二种用了two pointer, 第一个pointer到头时，第二个刚好停在要删的节点之前

两种都要用dummy head，避免edge case

Time: O(n)
Space: O(1)
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = ListNode(1)
prev = head
for i in range(4):
    prev.next = ListNode(i + 2)
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
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        cur = head
        dummy = ListNode(-1)
        dummy.next = head
        if n == length:
            temp = head.next
            dummy.next = temp
            head.next = None
        i = 1
        while i < length - n:
            cur = cur.next
            i += 1
        if cur.next:
            temp = cur.next.next
            cur.next.next = None
            cur.next = temp
        return dummy.next


    def removeNthFromEnd2(self, head, n):
        if n == 0:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pointer1 = head
        pointer2 = dummy
        count = 1
        while pointer1.next:
            if count >= n:
                pointer2 = pointer2.next
            pointer1 = pointer1.next
            count += 1
        temp = pointer2.next.next
        pointer2.next.next = None
        pointer2.next = temp
        return dummy.next


printList(head)
a = Solution()
printList(a.removeNthFromEnd2(head, 2))
