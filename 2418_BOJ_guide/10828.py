# 스택 [실버 4]

import sys
from collections import deque
input=sys.stdin.readline

N=int(input().rstrip())
dq=deque()
for _ in range(N):
    cmd=list(input().split())
    if cmd[0]=='push':
        dq.append(int(cmd[1]))
    elif cmd[0]=='top':
        print(dq[-1]) if len(dq)>0 else print(-1)
    elif cmd[0]=='size':
        print(len(dq))
    elif cmd[0]=='empty':
        print(1) if len(dq)==0 else print(0)
    elif cmd[0]=='pop':
        print(dq.pop()) if len(dq)!=0 else print(-1)
