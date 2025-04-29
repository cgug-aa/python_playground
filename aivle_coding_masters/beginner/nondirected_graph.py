# 무방향 그래프 1

import sys
input=sys.stdin.readline

N, M=map(int, input().split())
vertex=[[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    vertex[a-1][b-1]=1
    vertex[b-1][a-1]=1
for v in vertex:
    print(str(v).replace('[','').replace(']','').replace(',','')+' ')