# 그룹 ID

# N, M = map(int, input().split())
# graph=[[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# visit=[False]* (N+1)

# def dfs(graph, v, visit, group):
#     visit[v]=True
#     group.append(v)
#     for g in graph[v]:
#         if not visit[g]:
#             dfs(graph, g, visit ,group)
# min_id=N
# max_len=0
# for i in range(1, N+1):
#     group=[]
#     if visit[i]:
#         continue
#     dfs(graph, i, visit, group)
#     print(group)
#     if max_len<len(group):
#         max_len=len(group)
#         min_id=min(group)
#     elif max_len==len(group):
#         min_id=min(min_id, min(group))
#     if sum(visit)==N:
#         break
# print(min_id)
############################################################

N, M = map(int, input().split()) 
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (N+1)

def dfs(graph, v, visit, group):
    visit[v] = True
    group.append(v)
    for g in graph[v]:
        if not visit[g]:
            dfs(graph, g, visit, group)  # return 제거

max_len = 0
result = N + 1

for i in range(1, N+1):
    if visit[i]:
        continue
    group = []
    dfs(graph, i, visit, group)
    if len(group) > max_len:
        max_len = len(group)
        result = min(group)
    elif len(group) == max_len:
        result = min(result, min(group))  # 가장 작은 ID로 갱신

print(result)
