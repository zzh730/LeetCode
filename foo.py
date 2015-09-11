
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        fake = ListNode(0)
        fake.next = head
        pre, cur = None, fake
        while cur.next:
            if cur.next.val > x and not pre:
                pre = cur
            elif cur.next.val <= x:
                if pre:
                    temp = pre.next
                    pre.next = cur.next
                    cur.next = cur.next.next
                    pre.next.next = temp
                    pre = pre.next
                    continue
            cur = cur.next
        return fake.next

def makelist(arr):
    head = ListNode(arr[0])
    cur = head
    for i in arr[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head

def printlist(head):
    res = ''
    while head:
        res += str(head.val)+'->'
        head = head.next
    print( res[:-2])

arr = [2,1]
head = makelist(arr)
printlist(head)

a = Solution()
head = a.partition(head, 1)
printlist(head)