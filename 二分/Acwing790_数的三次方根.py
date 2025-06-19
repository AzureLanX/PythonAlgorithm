"""
@author:JuferBlue
@file:Acwing790_数的三次方根.py
@date:2025/6/19 12:10
@description:
"""

n = float(input())
l = -30.0
r = 30.0

while r-l>1e-8:
    mid = (l+r)/2.0
    if mid**3>=n:
        r = mid
    else:
        l = mid

print("{:.6f}".format(l))