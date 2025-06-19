"""
@author:JuferBlue
@file:Ac907_区间覆盖问题.py
@date:2025/6/19 20:09
@description:
"""

s,t = map(int,input().split())
n = int(input())

ranges = []

for i in range(n):
    a,b = map(int,input().split())
    ranges.append([a,b])

ranges.sort()


result = 0
cur_end = s
next_end = s
i = 0
while cur_end <t:
    found = False

    while i <n and ranges[i][0]<=cur_end:
        next_end = max(next_end,ranges[i][1])
        i += 1
        found = True

    if not found:
        result = -1
        break

    result+=1
    cur_end = next_end


# 处理 t == s 的特殊情况（目标是点）
if s == t:
    ok = False
    for l, r in ranges:
        if l <= s and r >= s:
            ok = True
            break
    print(1 if ok else -1)
else:
    print(result)