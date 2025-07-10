# 격자판 칠하기

N, M = map(int, input().split())
# 색깔 인덱스 1, 2, 3
field=[[0]*M for _ in range(N)]
cnt=0
dy=[0,-1]
dx=[-1,0]

def chk(y, x, color):
    for i in range(2):
        by=y+dy[i]
        bx=x+dx[i]
        if 0<=by<N and 0<=bx<M:
            if field[by][bx]==color:
                return False
    return True
                
def dfs(y, x):
    global cnt
    if y==N:
        cnt+=1
        return
    ny, nx = (y, x+1) if x+1 <M else (y+1, 0)

    for color in range(1, 4):
        if chk(y, x, color):
            field[y][x]=color
            dfs(ny, nx)
            field[y][x]=0  # 백트래킹

dfs(0, 0)
print(cnt)

'''
1. 색칠 조건 확인이 잘못됨
    if field[y][x] != field[ny][nx]:
지금 이 조건은 이동하기 전에 칠해져 있지 않은 곳의 색을 검사하고 있음
그런데 아직 field[ny][nx]는 색칠되지 않았으므로 무조건 0이라, 의미가 없음
즉, 현재 칸을 칠하고, 이전 칸들과의 색 겹침을 검사해야 함

2. 칸을 칠하고 다시 지우는 로직이 잘못됨
    field[y][x] = 0  ← 이건 현재 칸이 아니라 이전 칸을 지워버리는 구조
칠한 후 재귀를 돌릴 땐 field[ny][nx] = color로 칠하고,
재귀 후 되돌릴 때 0으로 바꿔야 함

######################### 이전 코드 ########################
# 색깔 인덱스 1, 2, 3
field=[[0]*M for _ in range(N)]
cnt=0
dy=[0,1]
dx=[1,0]
def recur(x, y):
    print(x, y)
    global cnt
    if y==N-1 and x==M-1:
        cnt+=1
        return
    for i in range(2):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<N and 0<=nx<M:
            for i in range(1, 4):
                if field[y][x]!=field[ny][nx]:
                    recur(nx, ny)
                    field[y][x]=0
                
                

for i in range(1, 4):
    field[0][0]=i
    recur(0, 0)
print(cnt)
'''