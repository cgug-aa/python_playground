# DFS와 BFS [실버 2]

import sys
from collections import defaultdict
input = sys.stdin.readline

N, M, V = map(int, input().split())
edges=defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for edge in edges.values():
    edge.sort()  
#DFS
def dfs(v):
    visited[v]=True
    print(v, end=' ')
    for e in edges[v]:
        if not visited[e]:
            visited[e]=True
            dfs(e)

visited=[False for _ in range(N+1)]
dfs(V)
print('')
#BFS
def bfs(v):
    visited[v]=True
    q = []
    q.append(v)
    print(v, end=' ')
    while q:
        en = q.pop(0)
        for e in edges[en]:
            if not visited[e]:
                q.append(e)
                visited[e]=True
                print(e, end=' ')

visited=[False for _ in range(N+1)]
bfs(V)