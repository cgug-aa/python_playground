# 묵찌빠봇
from collections import deque
N, M = map(int, input().split())
R1=deque(map(int, input().split()))
R2=deque(map(int, input().split()))

winner=0
count=len(R1)*len(R2)
# 가위:1, 바위:2, 보:3
while count>0:

    tmp=R1[0]-R2[0]
    
    #2가 이김
    if tmp==-1 or tmp==2:
        winner=2

    #1이 이김  
    elif tmp==1 or tmp==-2:
        winner=1

    #같은걸 냄
    else:
        if winner:
            break
    R1.rotate(-1)
    R2.rotate(-1)

    count-=1
if count==0:
    print(0)
else:
    print(winner)