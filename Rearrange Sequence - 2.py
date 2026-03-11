# Rearrange Sequence - 2 You are given an array of size N containing integers which may not be unique. Find the size of the largest subarray that can be rearranged to form a strictly contiguous sequence.
import sys
input=sys.stdin.readline
t= int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    b=1
    for i in range(n):
        mn=mx=arr[i]
        s=set()
        for j in range(i,n):
            if arr[j] in s:
                break
            s.add(arr[j])
            mn=min(mn,arr[j])
            mx=max(mx,arr[j])
            l=j-i+1
            if mx-mn==l-1:
                b=max(b,l)
    print(b)
