def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=" ")
    
    for g in graph[v]:
        if not visited[g]:
            dfs(graph, g, visited)

graph=[[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited=[False for _ in range(len(graph))]
dfs(graph, 1, visited)