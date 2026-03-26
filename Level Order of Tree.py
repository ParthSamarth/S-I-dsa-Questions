from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def insert(root,x):
    if not root:
        return Node(x)
    if x< root.val:
        root.left=insert(root.left,x)
    
    elif x > root.val:
        root.right=insert(root.right,x)
    return root
def level_order(root):
    if not root:
        return 
    q= deque([root])
    while q:
        size = len(q)
        level=[]
        for _ in range(size):
            node=q.popleft()
            level.append(str(node.val))
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(" ".join(level))
t= int(input())
for ti in range(t):
    n= int(input())
    arr=list(map(int,input().split()))
    root=None
    for x in arr:
        root=insert(root,x)
    level_order(root)
    if ti!=t-1:
        print()