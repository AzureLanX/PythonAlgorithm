"""
@author:JuferBlue
@file:差分矩阵.py
@date:2025/6/19 14:18
@description:
"""
N = 1010

n,m,q = map(int,input().split())

a = [[0]*N for _ in range(N)]
b = [[0]*N for _ in range(N)]

# 输入
for i in range(n):
    a[i+1][1:m+1] = map(int,input().split())

#
for i in range(1,n+1):
    for j in range(1,m+1):
        b[i][j] = a[i][j] - a[i-1][j] - a[i][j-1] + a[i-1][j-1]


while q:
    q-=1

    x1,y1,x2,y2,c = map(int,input().split())
    b[x1][y1] += c
    b[x2+1][y2+1] += c
    b[x1][y2+1] -= c
    b[x2+1][y1] -= c

for i in range(1,n+1):
    for j in range(1,m+1):
        b[i][j] = b[i][j] + b[i-1][j] + b[i][j-1] - b[i-1][j-1]
    print(*b[i][1:m+1])

