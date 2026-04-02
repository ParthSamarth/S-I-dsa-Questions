import sys
input=sys.stdin.readline

heap=[]
def insert(x):
    heap.append(x)
    i=len(heap)-1
    while i>0:
        p=(i-1)//2
        if heap[p]> heap[i]:
            heap[p],heap[i]=heap[i],heap[p]
            i=p  
        else:
            break
def heapify(i):
    n=len(heap)
    while True:
        s=i
        l=2*i+1
        r=2*i+2
        if l<n and heap[l]<heap[s]:
            s=l
        if r<n and heap[r]<heap[s]:
            s=r
        if s!=i:
            heap[s],heap[i]=heap[i],heap[s]
            i=s
        else:
            break
def delMin():
    if not heap:
        return
    heap[0]=heap[-1]
    heap.pop()
    if heap:
        heapify(0)
def getMin():
    if not heap:
        return "Empty"
    return heap[0]
t=int(input())

for _ in range(t):
    heap.clear()
    n,k=map(int,input().split())
    arr=map(int,input().split())
    for x in arr:
        insert(x)
    for _ in range(k-1):
        delMin()
    print(getMin())