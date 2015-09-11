__author__ = 'drzzh'





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
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head:
            return None
        if not head.next:
            return head
        fakeHead = ListNode(-1)
        fakeHead.next = head
        cur = head
        prev = fakeHead
        while cur:
            if cur.next:
                temp = cur.next
                prev.next = cur.next
                cur.next = cur.next.next
                temp.next = cur
                prev = cur
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return fakeHead.next




heada = construct([1,2,3,4,5,])
printList(heada)
a = Solution()
printList(a.swapPairs(heada))