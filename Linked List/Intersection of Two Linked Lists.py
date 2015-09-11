__author__ = 'drzzh'

'''
 两种算法
    1， 把链表翻转，找到交点，然后再翻转，
        Time: O(2n+2m)
    2. 先求俩链表长度，然后长链表先走，一样时开始同时移动找交点
        Time: O(m+n+max(m,n))

'''



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
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        headA = self.reverse(headA)
        headB = self.reverse(headB)

        cur1 = headA
        cur2 = headB
        result = None
        while cur1 and cur2:
            if cur1.val != cur2.val:
                headA = self.reverse(headA)
                headB = self.reverse(headB)
                return result
            else:
                result = cur1
                cur1 = cur1.next
                cur2 = cur2.next
        headA = self.reverse(headA)
        headB = self.reverse(headB)
        return result



    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev






'''






heada = construct([1,2,3,4,5,6,7,8,9,10,11,12,13])
headb = construct([4,5,6,7,8,9,10,11,12,13])



a = Solution()
print(a.getIntersectionNode(heada, headb).val)

printList(heada)
printList(headb)
'''

class another:
    def getIntersectionNode(self, headA, headB):
        cur1 = headA
        cur2 = headB
        lengthA = 0
        lengthB = 0
        while cur1:
            lengthA += 1
            cur1 = cur1.next
        while cur2:
            lengthB += 1
            cur2 = cur2.next
        count = lengthA - lengthB
        if lengthA > lengthB:
            cur1 = headA
            cur2 = headB
        else:
            cur1 = headB
            cur2 = headA
            count *= -1
        result = None
        while cur1:
            if count:
                cur1 = cur1.next
                count -= 1
                continue
            if cur1.val == cur2.val and not result:
                result = cur1
            elif cur1.val == cur2.val:
                pass
            else:
                result = None
            cur1 = cur1.next
            cur2 = cur2.next
        return result


heada = construct([1])
headb = construct([1])



a = another()
print(a.getIntersectionNode(None, None))


