__author__ = 'drzzh'

'''
翻转linked list, iterative方法需要用三个pointer，cur, temp, previous
    Time:O(n)
    Space:O(1)


    翻转部分linkedlist需要考虑很多case，可以有如下思考
        1.在head前加入fakehead,这样可以避免越界
        2.start用来记录m-1的list，翻转之后连接previous
        3.tail用来记录n+1的list，翻转之后接start.next

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head:
            return None
        if not head.next:
            return head
        if m == n:
            return head
        fakeHead = ListNode(-1)
        fakeHead.next = head
        start = fakeHead
        count1 = 1
        cur = head
        tail = None
        previous = None
        while (count1 <= n + 1): #trick,有时候n是最后一个list，为了运行到条件，必须多一次运行
            if count1 < m - 1:
                cur = cur.next
            elif count1 == m - 1:
                start = cur
                cur = cur.next
            elif count1 > n:
                if start.next and tail:
                    start.next.next = tail     #先tail，在start
                start.next = previous
                break
            else:
                if count1 == n:
                    tail = cur.next
                temp = cur.next
                cur.next = previous
                previous = cur
                cur = temp
            count1 += 1
        return fakeHead.next


head = ListNode(1)
'''
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

'''

a = Solution()

test = a.reverseBetween(head, 1, 1)
while (test):
    print(test.val)
    test = test.next
