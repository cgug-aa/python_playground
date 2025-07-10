# 그림

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
visit =[[False]*m for _ in range(n)]

dy=[0, -1, 0, 1]
dx=[1, 0, -1, 0]

def bfs(y, x):
    rs=1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if field[ny][nx]==1 and not visit[ny][nx]:
                    rs+=1   
                    visit[ny][nx]=True
                    q.append((ny, nx))
    return rs

cnt=0
maxv=0
for y in range(n):
    for x in range(m):
        if field[y][x]==1 and not visit[y][x]:
            visit[y][x]=True
            cnt+=1
            maxv=max(bfs(y, x), maxv)
print(cnt)
print(maxv)