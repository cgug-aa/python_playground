# I AM IRONMAN [실버 4]

import sys
from collections import defaultdict
input=sys.stdin.readline

N , P = map(int, input().split())
W, L, G = map(int, input().split())
players=defaultdict(int)
for _ in range(P):
    p, s = input().split()
    players[p]= W if s=='W' else -L

point=0
for _ in range(N):
    p=input().rstrip()
    if p in players.keys():
        point+=players[p]
    else:
        point-=L
    if point>=G:
        break
    point=max(0, point)

if point>=G:
    print('I AM NOT IRONMAN!!')
else:
    print('I AM IRONMAN!!')