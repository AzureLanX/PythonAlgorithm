"""
@author:JuferBlue
@file:Acwing801_二进制中1的个数.py
@date:2025/6/19 14:45
@description:
"""

n = int(input())

data = list(map(int,input().split()))

def one_count(x):
    cnt = 0

    while x:
        x-=(x&-x)
        cnt+=1

    return cnt
for x in data:
    print(one_count(x),end = " ")
