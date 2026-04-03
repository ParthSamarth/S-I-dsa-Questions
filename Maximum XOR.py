class TrieNode:
    def __init__(self):
        self.child=[None,None]
def insert(root,num):
        node =root
        for i in range(31,-1,-1):
            bit =(num>>i)&1
            if not node.child[bit]:
                node.child[bit]=TrieNode()
            node = node.child[bit]
def max_xor(root,num):
    node =root
    res=0
    for i in range(31,-1,-1):
            bit =(num>>i)&1
            op=1-bit
            if node.child[op]:
                res|=(1<<i)
                node=node.child[op]
            else:
                node = node.child[bit]
    return res
t=int(input())
for _ in range(t):
    n=int(input())
    arr= list(map(int,input().split()))
    root=TrieNode()
    insert(root,arr[0])
    ans =0
    for i in range(1,n):
        ans=max((ans,max_xor(root,arr[i])))
        insert(root,arr[i])
    print(ans)



    