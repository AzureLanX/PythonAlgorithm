"""
@author:JuferBlue
@file:Acwing796_子矩阵的和.py
@date:2025/6/19 13:25
@description:
"""

N=1010

a = [[0]*N for _ in range(N)]
s = [[0]*N for _ in range(N)]

n,m,q = map(int,input().split())

# 二维数组输入的处理
for i in range(1,n+1):
    a[i][1:m+1] =[int(x) for x in input().split()]

# 处理前缀和
for i in range(1,n+1):
    for j in range(1,m+1):
        s[i][j] = a[i][j]+s[i-1][j]+s[i][j-1]-s[i-1][j-1]

while q:
    q-= 1

    x1,y1,x2,y2 = map(int ,input().split())
    print(s[x2][y2]-s[x1-1][y2]-s[x2][y1-1]+s[x1-1][y1-1])
