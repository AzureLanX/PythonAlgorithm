"""
@author:JuferBlue
@file:Acwing797_差分.py
@date:2025/6/19 13:50
@description:
"""

N = 100010
n,m = map(int, input().split())

a = [0]*N
d = [0]*N
a[1:n+1] = map(int, input().split())
# 处理差分
for i in range(n):
    d[i+1] = a[i+1]-a[i]

while m:
    m-=1
    l,r,c = map(int, input().split())

    d[l]+=c
    d[r+1]-=c

# 恢复差分
for i in range(n):
    d[i+1] = d[i+1]+d[i]

#输出
print(*d[1:n+1])