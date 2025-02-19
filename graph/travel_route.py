# 여행 경로 프로그래머스 [레벨 3]
from itertools import permutations

tickets1=[["ICN", "JFK"],["HND", "IAD"],["JFK", "HND"]]
tickets2=[["ICN", "SFO"],["ICN", "ATL"], ["SFO","ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))
    case_list=permutations(tickets)
    for c in case_list:
        answer=[]
        for ticket in c:
            if len(answer)==0:
                answer.append(ticket[0])
                answer.append(ticket[1])
            else:
                if answer[-1]!=ticket[0]:
                    break
                answer.append(ticket[1])

        if len(answer)-1==len(tickets):
            return answer
        
print(solution(tickets1))
print(solution(tickets2))

"""
내 풀이: 모든 경우의 수를 생성한 뒤, 코드를 돌리기 때문에 비효율적 -> 시간 초과

->DFS 단원이니만큼 DFS
from collections import defaultdict
def solution(tickets):
    routes=defaultdict(list)
    
    for key, value in tickets:
        routes[key].append(value)

    # 딕셔너리의 값을 사전순으로 정렬   
    routes={key:sorted(value) for key, value in routes.items()}


    stack=['ICN'] #DFS 탐색용(미완성 경로 저장)
    path=[]       #최종 경로 저장용(완성 경로)
    while stack:
        top=stack[-1]
        if top not in routes or not routes[top]:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop(0))
    return path[::-1]

"""