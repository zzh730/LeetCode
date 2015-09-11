__author__ = 'drzzh'
'''
因为是BST所以就省去了验证节点是否存在的function， 直接判断值大小即可判断包不包含节点

Time:O(h)
'''


def LCA(root,p,q):
    if not root or not q or not p:
        return None
    if max(q.val,p.val) < root.val:
        return LCA(root.left,p,q)
    elif min(q.val,p.val) < root.val <max(q.val,p.val):
        return root
    elif min(p.val,q.val) > root.val:
        return LCA(root.right,p,q)