import sys
input=sys.stdin.readline
t=int(input())
res=[]
def Kadane(arr):
    ms=arr[0]
    cs=arr[0]
    for i in range(1,len(arr)):
        cs=max(arr[i],cs+arr[i])
        ms=max(ms,cs)
    return ms

for _ in range(t):
    n,m=map(int,input().split())

    mat=[list(map(int,input().split())) for _ in range(n)]
    mx=-10**18
    for i in range(n):
        temp=[0]*m

        for j in range(i,n):
            for c in range(m):
                temp[c]+=mat[j][c]
            mx=max(mx,Kadane(temp))

    res.append(str(mx))

print("\n".join(res))