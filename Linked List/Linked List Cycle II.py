__author__ = 'drzzh'


'''
    这题要求找到环的起点， 思路是：
        当发现环时中断循环，
        fast = head、
        当俩pointer相遇时，就是环的起点

        2s = l + n + c
        s = l + n
        ==> c - n = l

'''


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                break
        else:
            return None
        while fast:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
