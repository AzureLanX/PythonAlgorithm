"""
@author:JuferBlue
@file:S2.py.py
@date:2025/6/19 21:46
@description:
"""
n = int(input())

score = [0] * 21

for i in range(n):
    for j in range(20):
        p,k = map(int,input().split())
        if p==1:
            score[j] = score[j] + k + 12
        elif p==2:
            score[j] = score[j] + k + 9
        elif p==3:
            score[j] = score[j] + k + 7
        elif p==4:
            score[j] = score[j] + k + 5
        elif p==5:
            score[j] = score[j] + k + 4
        elif p>=6 and p <= 7:
            score[j] = score[j] + k + 3
        elif p>=8 and p<=10:
            score[j] = score[j] + k + 2
        elif p>=11 and p<=15:
            score[j] = score[j] + k + 1
        elif p>=16 and p<=20:
            score[j] = score[j] + k

for i in range(1,21):
    print(i,score[i])
