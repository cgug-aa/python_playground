# 야바위
import sys
input=sys.stdin.readline

N,M=map(int, input().split())
cups=[i for i in range(1, N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    tmp = cups[a-1]
    cups[a-1]=cups[b-1]
    cups[b-1]=tmp
tgt = int(input().rstrip())
print(cups.index(tgt)+1)
