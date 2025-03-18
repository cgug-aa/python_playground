# 상근이의 여행 [실버 4]

from collections import deque, defaultdict
import sys
input=sys.stdin.readline

T=int(input().rstrip())
for _ in range(T):
    N, M = map(int, input().split())
    edge=defaultdict(list)

    for _ in range(M):
        a, b =map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)

    visited=[0]*(N+1)
    
    queue=deque([1])
    visited[1]=1
    count=0

    while sum(visited)!=N:
        q=queue.popleft()
        for e in edge[q]:
            if visited[e]==0:
                visited[e]=1
                queue.append(e)
                count+=1

    print(count)