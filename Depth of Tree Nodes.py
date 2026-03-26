class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def insert(root,x,depth):
    if not root:
        return Node(x),depth
    if x< root.val:
        root.left,d =insert(root.left,x,depth+1)
    
    elif x > root.val:
        root.right,d =insert(root.right,x,depth+1)
    return root,d
t= int(input())
for ti in range(t):
    n= int(input())
    arr=list(map(int,input().split()))
    root=None
    res=[]
    for x in arr:
        root,d=insert(root,x,0)
        res.append(str(d))
    print(" ".join(res))