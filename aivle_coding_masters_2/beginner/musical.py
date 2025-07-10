# 뮤지컬 - 이중포인터 = 슬라이딩 윈도우

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
days = list(map(int, input().split()))
minv=N
for i in range(N):
    actor=set()
    day=0
    j=i
    while len(actor)<K and j<N:
        actor.add(days[i])
        day+=1
        j+=1
    if len(actor)==K:
        minv=min(minv, day)

print(minv)