"""
@author:JuferBlue
@file:Acwing799_连续不重复子序列.py
@date:2025/6/19 16:35
@description:
"""

n = int(input())

arr = list(map(int,input().split()))
hash = [0]*100010
j = 0
result = 0
for i in range(n):
    hash[arr[i]]+=1
    while j<i and hash[arr[i]]>1:
        hash[arr[j]]-=1
        j+=1
    result = max(result,i-j+1)

print(result)
