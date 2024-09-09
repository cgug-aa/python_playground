# 바이러스 [실버 3]

#노드 수
N=int(input())

#엣지 수
E=int(input())

#엣지
edge_adj=[[] for _ in range(N+1)]
for _ in range(E):
    new_edge=list(map(int, input().split()))
    edge_adj[new_edge[0]].append(new_edge[1])
    edge_adj[new_edge[1]].append(new_edge[0])

#감염 여부
inf=[0 for _ in range(N+1)]

def search(n):
    inf[n]=1
    for w in edge_adj[n]:
        if inf[w]==0:
            inf[w]=1
            search(w)

search(1)

print(sum(inf)-1)