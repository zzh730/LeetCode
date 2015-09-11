__author__ = 'drzzh'

from collections import deque

'''
    level order traversal
    Time: O(n)
    Space: O(n)
'''


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return
        stack1 = deque([root])
        stack2 = []
        count1 = 1
        count2 = 0
        while stack1:
            cur = stack1.popleft()
            count1 -= 1
            if cur.left:
                stack1.append(cur.left)
                stack2.append(cur.left)
                count2 += 1
            if cur.right:
                stack1.append(cur.right)
                stack2.append(cur.right)
                count2 += 1
            if count1 == 0:
                if not stack2:
                    continue
                if len(stack2) > 1:
                    for index in range(1, len(stack2)):
                        stack2[index - 1].next = stack2[index]
                count1 = count2
                count2 = 0
                stack2 = []


'''
    不记录每层的节点，用俩指针保存，只存最关键的
    Time: O(n)
    Space: O(1)
'''
class Solution2:
    def connect1(self, root):
        prev = None
        cur = root
        head = None
        while cur:
            while cur:
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right
                cur = cur.next
            cur = head
            prev = None
            head = None
