# 네트워크 프로그래머스 [레벨 3]

n1=3
computers1=[
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

def solution(n, computers):
    visited=[0 for _ in range(n)]
    answer=0


    for node in range(n):
        if visited[node]==0:
            stack=[node]
            visited[node]=1

            while stack:
                cur=stack.pop()
                for next_node in range(n):
                    if(not visited[next_node] and computers[cur][next]==1):
                        visited[next_node]=1
                        stack.append(next_node)
            answer+=1
    return answer

'''
풀이: stack을 통해 방문하는 경로를 나타낸다. 
'''