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

def pre(root):
    if not root:
        return []
    return  [root.val]+pre(root.left)+pre(root.right)
def trim(root,l,r):
    if not root:
        return None
    if root.val<l:
        return trim(root.right,l,r)
    if root.val>r:
        return trim(root.left,l,r)
    root.left=trim(root.left,l,r)
    root.right=trim(root.right,l,r)
    return root

t= int(input())
for ti in range(t):
    n,l,r= map(int,input().split())
    arr=list(map(int,input().split()))
    root=None
    for x in arr:
        root=insert(root,x)
    root=trim(root,l,r)
    res= pre(root)
    print(*res)
    
