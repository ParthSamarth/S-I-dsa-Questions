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

def find_min(root):
    while root.left:
        root=root.left
    return root

def delete(root,x):
    if not root:
        return None
    if x< root.val:
        root.left=delete(root.left,x)
    
    elif x > root.val:
        root.right=delete(root.right,x)
    else:
        if not root.left:
            return root.right
        
        elif not root.right:
            return root.left
        else:
            temp = find_min(root.right)
            root.val=temp.val
            root.right=delete(root.right,temp.val)
    return root

def search(root,x):
    if not root:
        return False
    if root.val==x:
        return True

    elif x< root.val:
        return search(root.left,x)
    
    else:
        return search(root.right,x)

def pre(root,res):
    if not root:
        return
    res.append(str(root.val))
    pre(root.left,res)
    pre(root.right,res)

t= int(input())
for ti in range(t):
    q= int(input())
    root=None
    print(f"Case #{ti+1}:")
    for _ in range(q):
        arr=input().split()
        typ=int(arr[0])
        if typ == 1:
            x=int(arr[1])
            root=insert(root,x)
        elif typ==2:
            x=int(arr[1])
            root=delete(root,x)
        elif typ==3:
            x=int(arr[1])
            print("Yes" if search(root,x) else "No")
        elif typ==4:
            res=[]
            pre(root,res)
            if res:
                print(" ".join(res))
            else:
                print("null")