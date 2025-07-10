# 단지번호 붙이기

import sys
input=sys.stdin.readline

N = int(input())
field=[list(map(int, list(input().rstrip()))) for _ in range(N)]
visit=[[False]*N for _ in range(N)]

dy=[0, 1, 0, -1]
dx=[1, 0, -1, 0]
def dfs(y, x):
    global size
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=nx<N and 0<=ny<N:
            if field[ny][nx]==1 and not visit[ny][nx]:
                visit[ny][nx]=True
                size+=1
                dfs(ny, nx)
sizes=[]
cnt=0
for y in range(N):
    for x in range(N):
        if field[y][x]==1 and not visit[y][x]:
            visit[y][x]=True
            cnt+=1
            size=1
            dfs(y, x)
            sizes.append(size)
print(cnt)
for v in sorted(sizes):
    print(v)