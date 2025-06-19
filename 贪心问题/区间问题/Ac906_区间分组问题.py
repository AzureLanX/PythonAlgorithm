"""
@author:JuferBlue
@file:Ac906_区间分组问题.py
@date:2025/6/19 19:05
@description:
"""
# ✅ 正确思路：贪心 + 小根堆（优先队列）
# 1. 先对所有区间按左端点排序
# 因为我们想从最早开始的区间，按顺序来安排组。
#
# 2. 用一个最小堆（小根堆）维护每个组的“最后一个区间的右端点”
# 当前新来的区间 [l, r]，只要它能接在某个组最后一个区间的后面（即 l > 组的右端点），就可以放进去。
#
# 如果不行，就开新组。
import heapq
n = int(input())

ranges = []

for i in range(n):
    l,r = map(int, input().split())
    ranges.append([l,r])

ranges.sort()

heap = []

for l,r in ranges:
    if heap and l>heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap,r)
    else:
        heapq.heappush(heap,r)

print(len(heap))


