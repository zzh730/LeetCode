__author__ = 'drzzh'

'''
    从中间开始反转list然后比较即可

    Time: O(n)
    Space: O(1)

'''


class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        new = self.reverse(slow)
        cur1 = head
        cur2 = new
        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True

    def reverse(self, root):
        prev = None
        cur = root
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
