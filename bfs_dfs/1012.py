# 유기농 배추

import sys
input=sys.stdin.readline

def bfs(y, x):
    q=[]
    q.append((y, x))
    visit[y][x]==True

    while q:
        ey, ex = q.pop()
        for i in range(4):
            ny=ey+dy[i]
            nx=ex+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if not visit[ny][nx] and field[ny][nx]==1:
                    q.append((ny, nx))
                    visit[ny][nx]=True


T = int(input().rstrip())

dy=[0, 1, 0, -1]
dx=[1, 0 , -1, 0]


for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    visit = [[False]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x]=1
    
    count=0
    for y in range(N):
        for x in range(M):
            if not visit[y][x] and field[y][x]==1:
                bfs(y, x)
                count+=1
    
    print(count)