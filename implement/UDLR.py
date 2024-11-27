# 상하좌우 [난이도 1]

N=int(input())
cmd=list(input().split())
point=[1, 1]

# 내 풀이
for c in cmd:
    if c=='U':
        point[0]-=1 if point[0]>1 else 0
    elif c=='D':
        point[0]+=1 if point[0]<N else 0
    elif c=='L':
        point[1]-=1 if point[1]>1 else 0
    elif c=='R':
        point[1]+=1 if point[1]<N else 0

print(point[0], point[1])

# sol
n=int(input())
x, y=1, 1
plans=input().split()

dy=[-1, 1, 0, 0]
dx=[0, 0, -1, 1]
move_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]      #이동 후 위치
            ny=y+dy[i]      
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x, y=nx, ny
print(x, y)