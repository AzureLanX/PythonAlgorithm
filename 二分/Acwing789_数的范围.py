"""
@author:JuferBlue
@file:Acwing789_数的范围.py
@date:2025/6/19 8:56
@description:
"""


n,q = map(int,input().split())

data = [int(x) for x in input().split()]

while q:
    q-=1

    k = int(input())
    l = 0
    r = n-1
    while l<r:
        mid = l+r>>1
        if data[mid]>=k:
            r = mid
        else:
            l = mid+1

    if data[l]!=k:
        print("-1 -1")
    else:
        print(l,end = " ")
        l = 0
        r = n-1
        while l<r:
            mid = l+r+1>>1
            if data[mid]<=k:
                l = mid
            else:
                r = mid-1
        print(l)

