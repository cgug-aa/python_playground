# 큐 [실버 4]
from collections import deque
import sys
input=sys.stdin.readline

N=int(input().rstrip())
queue=deque()
for _ in range(N):
    command=list(input().split())
    if command[0]=='push':
        queue.append(int(command[1]))
    elif command[0]=='pop':
        print(queue.popleft()) if len(queue)!=0 else print(-1)
    elif command[0]=='size':
        print(len(queue))
    elif command[0]=='empty':
        print(1) if len(queue)==0 else print(0)
    elif command[0]=='front':
        print(queue[0]) if len(queue)!=0 else print(-1)
    elif command[0]=='back':
        print(queue[-1]) if len(queue)!=0 else print(-1)
    else:
        print("이해할 수 없는 명령")
        continue