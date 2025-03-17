# 알고리즘 수업 - 깊이 우선 탐색 2
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M, R = map(int, input().split())
edges=[]
answer=defaultdict(int)
visited=[0 for _ in range(N+1)]

for _ in range(M):
    edges.append(list(map(int, input().split())))
count=0

def dfs(visited, edges, R):
    global count
    count+=1
    visited[R]=1
    answer[R]=count
    adj=sorted([edges[idx][1] if edges[idx][0]==R else edges[idx][0] for idx in range(M) if R in edges[idx]], reverse=True)
    for a in adj:
        if visited[a]==0:
            dfs(visited, edges, a)

dfs(visited, edges, R)
for idx in range(1, N+1):
    print(answer[idx])

'''
풀이 결과: 시간 초과
-> 그래프를 인접 리스트로 미리 구성하지 않고, 매번 리스트를 순회하며 인접 노드를 찾기 때문
1. 간선을 저장하는 방식
    - edges 리스트에 모든 간선을 저장한 후, dfs 함수에서 현재 노드 R과 연결된 노드를 찾기 위해 매번 edges 리스트를 전체 순회(O(M))합니다.
    - 결과적으로 모든 노드를 방문하는 데 O(NM)의 시간이 걸릴 수 있습니다. (최악의 경우 𝑁=𝑀, N=M일 때 O(N²))
2. 인접 리스트를 사용하지 않음
    - dfs 함수를 호출 시마다 모든 간선을 검사하는 대신, 미리 인접리스트를 구성하면 O(1)에 가까운 시간 복잡도로 인접 노드를 찾을 수 있음
'''