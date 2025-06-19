"""
@author:JuferBlue
@file:Acwing803_区间合并.py
@date:2025/6/19 14:44
@description:
"""
class Range:
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def __lt__(self, other):
        return self.l < other.l


n = int(input())
ranges = []

result = []
for i in range(n):
    l,r = map(int, input().split())
    ranges.append(Range(l,r))

# 按左端点排序
ranges.sort()

st = -2e9
ed = -2e9

for i in range(n):
    if ranges[i].l>ed:
        if(st!=-2e9):
            result.append(Range(st,ed))
        st = ranges[i].l
        ed = ranges[i].r
    else:
        ed = max(ed, ranges[i].r)

# 加入最后一个
if st!=2e9:
    result.append(Range(st,ed))

# 输出区间个数
print(len(result))