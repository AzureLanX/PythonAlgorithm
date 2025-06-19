"""
@author:JuferBlue
@file:S1.py
@date:2025/6/19 21:07
@description:
"""
# 题目：https://blog.csdn.net/qq_60624992/article/details/140242368?utm_source=chatgpt.com


# 15 3
# 33 35 34 36 37 40 32 31 30 29 28 29 33 38 40

n,w = map(int,input().split())

temp = list(map(int,input().split()))


free_day = 0
fail_day = 0

for i in range(n):
    if (w+i)%7 !=4 and temp[i]>=35:
        free_day+=1
    elif (w+i)%7==4 and temp[i]>=35:
        fail_day+=1

print(free_day,fail_day)