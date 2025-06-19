"""
@author:JuferBlue
@file:Acwing800_数组元素的目标和.py
@date:2025/6/19 17:11
@description:
"""


n,m,x = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

i = 0
j = m-1

while(i<n and j>=0):
    temp= a[i]+b[j]
    if temp<x:
        i+=1
    elif temp>x:
        j-=1
    else:
        print(i,j)
        break

