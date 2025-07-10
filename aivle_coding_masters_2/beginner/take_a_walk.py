# 동네 한 바퀴

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visit=[False]*(N+1)

for _ in range(M):
    s, d = map(int, input().split())
    graph[s][d]=1


cnt=0
chk=False
def recur(num):
    global cnt, chk
    if cnt==M or sum(visit)==N:
        if num==1:
            chk=True
        return
    
    for i in range(1, N+1):
        if graph[num][i]==1:
            visit[num]=True
            cnt+=1
            recur(i)
recur(1)
print('YES' if chk else 'NO')
