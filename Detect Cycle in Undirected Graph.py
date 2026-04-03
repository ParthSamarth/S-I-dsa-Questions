import sys
input=sys.stdin.readline
def find(x,parent):
    if parent[x]!=x:
        parent[x]=find(parent[x],parent)
    return parent[x]

def union(x,y,parent,rank):
    px=find(x,parent)
    py=find(y,parent)
    if px!=py:
        if rank[px]<rank[py]:
            parent[px]=py
        elif rank[px]>rank[py]:
            parent[py]=px
        else:
            parent[py]=px
            rank[px]+=1

        
t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    parent=list(range(n+1))
    rank=[0]*(n+1)
    hc=False
    for _ in range(m):
        u,v=map(int,input().split())
        if find(u,parent)==find(v,parent):
            hc=True
        else:
            union(u,v,parent,rank)
    print(hc)
