# Rearrange Sequence - 3 bookmark_borderYou are given an array of size N containing integers. Find the size of the largest subarray that can be rearranged to form a contiguous sequence.
# A contiguous sequence means that the difference of adjacent elements should be 0 or 1.
import sys
input=sys.stdin.readline
t= int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    b=1
    for i in range(n):
        mn=mx=arr[i]
        for j in range(i,n):
            mn=min(mn,arr[j])
            mx=max(mx,arr[j])
            l=j-i+1
            if mx-mn<=l-1:
                b=max(b,l)
    print(b)
