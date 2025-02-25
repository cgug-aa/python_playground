# 회전하는 큐 [실버 3]

from collections import deque
import sys
input=sys.stdin.readline

N, M = map(int, input().split())
cqueue=deque([i for i in range(1, N+1)])
tgt=list(map(int, input().split()))
count=0

for t in tgt:
    if cqueue.index(t)<=len(cqueue)//2:
        while(t!=cqueue[0]):
            cqueue.rotate(-1)
            count+=1
    else:
        while(t!=cqueue[0]):
            cqueue.rotate(1)
            count+=1
            
    cqueue.popleft()
print(count)