__author__ = 'drzzh'


'''
    用队列实现BFS，注意队列中的元素（cur,newCur）
    Time: O(n^2)
    Space: O(n)


'''




from collections import deque


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        visited = {}
        newNode = UndirectedGraphNode(node.label)
        toVisit = deque([(node, newNode)])#tuple必须得有，如果没有新的节点，光凭visited[cur]不行，因为是新复制节点，不能保证一致性
        while toVisit:
            cur, newCur = toVisit.popleft()
            if cur in visited:
                continue
            else:
                visited[cur] = newCur
                for item in cur.neighbors:
                    newNeighbor = UndirectedGraphNode(item.label)
                    newCur.neighbors.append(newNeighbor)
                    toVisit.append((item, newNeighbor))
        return newNode