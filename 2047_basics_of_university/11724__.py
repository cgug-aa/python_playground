# 연결 요소의 개수 [실버 2]

# 풀이: DFS/BFS 수행 횟수가 연결요소의 개수

import sys
input=sys.stdin.readline
N, M=map(int, input().split())

graph=[[] for _ in range(N+1)]
for _ in range(M):
    u, v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


'''
edge=[]
for _ in range(M):
    edge.append(list(map(int, input().split())))

component=[]

for e in edge:
    print("edge :",e)
    
    if len(component)==0:
        component.append(set([e[0], e[1]]))
    else:
        for c in component:
            if e[0] in c or e[1] in c:
                c.update([e[0], e[1]])
                break
            else:
                component.append(set([e[0], e[1]]))
    
print(component)
print(len(component))'''