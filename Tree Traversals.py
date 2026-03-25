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

def pre(root,res):
    if not root:
        return
    res.append(str(root.val))
    pre(root.left,res)
    pre(root.right,res)
def post(root,res):
    if not root:
        return
    post(root.left,res)
    post(root.right,res)
    res.append(str(root.val))
def inorder(root,res):
    if not root:
        return
    inorder(root.left,res)
    res.append(str(root.val))
    inorder(root.right,res)

t= int(input())
for ti in range(t):
    n= int(input())
    arr=list(map(int,input().split()))
    root=None
    for x in arr:
        root=insert(root,x)
    p,pp,i=[],[],[]
    pre(root,p)
    post(root,pp)
    inorder(root,i)
    print(" ".join(p))
    print(" ".join(i))
    print(" ".join(pp))
    if ti!=t-1:
        print()

