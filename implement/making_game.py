# 게임 개발 [난이도 2]

import sys
input=sys.stdin.readline

#전체 맵의 세로/가로 길이
N, M= map(int, input().split())

#위치 및 바라보는 방향(N:0, E:1, S:2, W:3)
A, B, C= map(int, input().split())
pnt=[A, B]

#맵의 지형(0:육지, 1:바다)
Map=[]
for _ in range(N):
    Map.append(list(map(int, input().split())))

#방문여부
visited=[[False for _ in range(M)] for _ in range(N)]
# 이게 좋겠지?
# visited=[[False]*M for _ in range(N)]

visited[A][B]=True
rotate=0



# 아래 코드는 계산이 너무 많음
# 이동 방향을 리스트로 만들어주고
# C에따라 이동 후 위치를 적용해 가능한지 판단한다.
# 조건문을 이동가능한 경우 이동하는거로 하기
# 반대 경우는 계산이 너무 많음
# 






#########################


while True:
    #왼쪽으로 돌기
    C = C-1 if C>0 else 3
    rotate+=1
    if rotate>=4:
        C= C+1 if C<3 else 0
        if C==0:
            pnt[0]+=1
        elif C==1:
            pnt[1]-=1
        elif C==2:
            pnt[0]-=1
        elif C==3:
            pnt[1]+=1
        rotate=0
        if Map[pnt[0]][pnt[1]]==1 or (pnt[0] not in range(N) or pnt[1] not in range(M)):
            break
        
        continue

    if C==0:
        move=[pnt[0]-1, pnt[1]]
        if move[0] < 0 or visited[move[0]][move[1]]==True or Map[move[0]][move[1]]==1:
            continue
        else:
            rotate=0
            pnt=move
            visited[pnt[0]][pnt[1]]=True
    elif C==1:
        move=[pnt[0], pnt[1]+1]
        if move[1] > M-1 or visited[move[0]][move[1]]==True or Map[move[0]][move[1]]==1:
            continue
        else:
            rotate=0
            pnt=move
            visited[pnt[0]][pnt[1]]=True
    elif C==2:
        move=[pnt[0]+1, pnt[1]]
        if move[0] > N-1 or visited[move[0]][move[1]]==True or Map[move[0]][move[1]]==1:
            continue
        else:
            rotate=0
            pnt=move
            visited[pnt[0]][pnt[1]]=True        
    elif C==3:
        move=[pnt[0], pnt[1]-1]
        if move[1] < 0  or visited[move[0]][move[1]]==True or Map[move[0]][move[1]]==1:
            continue
        else:
            rotate=0
            pnt=move
            visited[pnt[0]][pnt[1]]=True
    print(C)
print(visited)