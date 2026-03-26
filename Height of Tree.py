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
def height(root):
    if not root:
        return -1
    return 1+ max(height(root.left),height(root.right))
t= int(input())
for ti in range(t):
    n= int(input())
    arr=list(map(int,input().split()))
    root=None
    for x in arr:
        root=insert(root,x)
    print(height(root))