# 점심시간 레이스 [브론즈 2]
import sys
input=sys.stdin.readline

n, m, k = map(int, input().split())
min_value= n + m
winner=1
for c in range(1,k+1):
    f, d = map(int, input().split())
    if min_value > f + m - d:
        min_value= f + m - d
        winner=c
print(winner)