__author__ = 'drzzh'

'''
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        fakehead = ListNode(-1)
        fakehead.next = head
        if not head or not head.next:
            return head
        cur, pCur = head.next, head
        while cur:
            nextStep = cur.next
            if cur.val < pCur.val:
                temp, prev = fakehead.next, fakehead
                while temp != pCur.next:
                    if cur.val < temp.val:
                        pCur.next = nextStep
                        prev.next = cur
                        cur.next = temp
                        break
                    prev = temp
                    temp = temp.next
            pCur = cur if cur.next == nextStep else pCur
            cur = nextStep
        return fakehead.next


def makeList(lst):
    head = ListNode(lst[0])
    cur = head
    for item in lst[1:]:
        cur.next = ListNode(item)
        cur = cur.next
    return head


def printList(head):
    while head:
        print(head.val)
        head = head.next
    print('----')


head = makeList([3, 2, 6, 4])

a = Solution()
printList(a.insertionSortList(head))
