
__author__ = 'drzzh'



from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(4)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(8)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(6)
tree.right.left.left = TreeNode(9)
tree.right.left.right = TreeNode(10)


class Node:
    def __init__(self, char=None, value=None):
        self.char = char
        self.value = value
        self.next = []

    def inNext(self, char):
        for child in self.next:
            if char == child.char:
                return True
        else:
            return False

    def get(self, char):
        for child in self.next:
            if char == child.char:
                return child
        else:
            print("Not Found!")


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, key):
        cur = self.root
        for char in word:
            if cur.inNext(char):
                cur = cur.get(char)
            elif char == word[-1]:
                temp = Node(char, key)
                cur.next.append(temp)
            else:
                temp = Node(char)
                cur.next.append(temp)
                cur = temp

    def delete(self, word):
        pass
    def find(self, word):
        pass

    def printTree(self):
        count1 = 1
        count2 = 0
        queue = deque([self.root])
        result = []
        temp = []
        while queue:
            cur = queue.popleft()
            temp.append(cur.char)
            count1 -= 1
            for item in cur.next:
                queue.append(item)
                count2 += 1
            if count1 == 0:
                result.append(temp)
                temp = []
                count1 = count2
                count2 = 0
        for item in result:
            print(item)


a = [1,2,3]
print(a[-2:])
