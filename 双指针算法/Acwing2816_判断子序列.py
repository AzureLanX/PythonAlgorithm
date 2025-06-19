
"""
@author:JuferBlue
@file:Acwing2816_判断子序列.py
@date:2025/6/19 17:53
@description:
"""


n,m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

i = j = 0

for j in range(m):
    if a[i] == b[j]:
        i += 1
    if i==n:
        print("Yes")
        # 结束程序
        exit()

print("No")

