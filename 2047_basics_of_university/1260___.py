#DFS와 BFS [실버 2]
#다시 풀기

# 정점 수: N, 간선 수: M,탐색을 시작할 정점 번호: V
N, M, V=map(int, input().split())
# edge
edge=set()
for _ in range(M):
    edge.add(tuple(map(int, input().split())))

edge=list(edge)
#인접 노드 추출
edge_adj=[[] for _ in range(N)]
for e in edge:
    edge_adj[e[0]-1].append(e[1])
    edge_adj[e[1]-1].append(e[0])
edge_adj.sort()

# DFS: 깊이 우선 탐색
DFS_visited=[0 for _ in range(N)]

def DFS(n):
    print(n, end=" ")
    DFS_visited[n-1]=1
    for w in edge_adj[n-1]:
        if DFS_visited[w-1]==0:
            DFS(w)

# BFS: 너비 우선 탐색
BFS_visited=[0 for _ in range(N)]

def BFS(n):
    print(n, end=" ")
    BFS_visited[n-1]=1
    for w in edge_adj[n-1]:
        if BFS_visited[w-1]==0:

DFS(V)
BFS(V)