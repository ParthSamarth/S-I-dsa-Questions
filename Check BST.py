from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def build(arr,n):
    nodes=[None]*(n+1)
    for i in range(1,n+1):
        nodes[i]=Node(arr[i-1])
    for i in range(1,n+1):
        if 2*i <=n:
            nodes[i].left=nodes[2*i]
        if 2*i+1 <=n:
            nodes[i].right=nodes[2*i+1]
    return nodes[1]
def is_bst(root,low,high):
    if not root:
        return True 
    if root.val<=low or root.val>=high:
        return False
    return (is_bst(root.left,low,root.val) and is_bst(root.right,root.val,high) )
t= int(input())
for ti in range(t):
    n= int(input())
    arr=list(map(int,input().split()))
    root=build(arr,n)
    print(is_bst(root,float('-inf'),float('inf')))
    