"""
@author:JuferBlue
@file:Acwing795_前缀和.py
@date:2025/6/19 12:30
@description:
"""

n,m = map(int,input().split())

arr = [0]*100010

arr[1:n+1] = [int(x) for x in input().split()]

for i in range(n):
    arr[i+1] = arr[i+1]+arr[i]

while m:
    m-=1
    l,r = map(int,input().split())
    print(arr[r]-arr[l-1])
