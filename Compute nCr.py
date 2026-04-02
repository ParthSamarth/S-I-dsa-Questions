import sys
input=sys.stdin.readline
mod=10**9+7
MAXN= 2000
dp=[[0]*(MAXN+1)for _ in range(MAXN+1)]
for i in range(MAXN+1):
    dp[i][0]=1
    for j in range(1,i+1):
        if j==i:
            dp[i][j]=1
        else:
            dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%mod

t=int(input())
res=[]
for _ in range(t):
    n,r=map(int,input().split())
    if r>n:
        res.append("0")
    else:
        res.append(str(dp[n][r]))

print("\n".join(res))