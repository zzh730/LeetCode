__author__ = 'drzzh'


'''
    merge sort的list版本，
    区别是，每次需要一个split list， 通过快慢指针来实现。
    merge就是cur和other来回切换，保证cur的那条list值一直是最小的
    注意：
        1. split list 需要断list
        2. merge时最后一个other如果存在要添加进末尾。

    Time: O(nlogn)
    Space: O(1)
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
    def sortList(self, head):
        if not head or not head.next:
            return head
        a, b = self.splitList(head)
        a = self.sortList(a)
        b = self.sortList(b)
        return self.merge(a, b)

    def splitList(self, head):
        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        return head, slow

    def merge(self, a, b):
        head = a if a.val < b.val else b
        other = b if head == a else a
        cur, prev = head.next, head
        while other and cur:
            if cur.val < other.val:
                prev = cur
                cur = cur.next
            else:
                prev.next = other
                other = cur
                cur = prev.next.next
                prev = prev.next
        if other:
            prev.next = other
        return head


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


head = makeList([6, 2, 5, 1, 3, 4])
printList(head)
a = Solution()
printList(a.sortList(head))
