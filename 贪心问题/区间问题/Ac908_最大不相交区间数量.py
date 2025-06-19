"""
@author:JuferBlue
@file:Ac908_最大不相交区间数量.py
@date:2025/6/19 18:24
@description:
"""
n = int(input())

ranges = []

for i in range(n):
    l,r = map(int,input().split())
    ranges.append([l,r])

ranges.sort(key = lambda x:x[1])

st = -2e9
result = 0
for i in range(n):
 if ranges[i][0]>st:
     result += 1
     st = ranges[i][1]

print(result)
