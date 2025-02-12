# 명예의 전당 프로그래머스 [레벨 1]

k1=3
scores1=[10, 100, 20, 150, 1, 100, 200]
k2=4
scores2=[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

def my_solution(k, scores):
    day_score=[]
    result=[]
    for s in scores:
        day_score.append(s)
        day_score.sort(reverse=True)
        result.append(day_score[-1] if len(day_score)<k else day_score[k-1])
    print(result)

my_solution(k1, scores1)
my_solution(k2, scores2)

'''
sol) 힙(최소힙)을 사용한 풀이
힙의 길이가 k 이하일 때는 바로 힙의 루트 값을 answer에 넣고,
힙의 길이가 k보다 커지면, 힙의 최소값을 제거한 후 루트값을 answer에 추가한다. 
import heapq
def solution(k, score):
    answer=[]
    rank=[]
    for sco in score:
        heapq.heappush(rank, sco)

        if len(rank)>k:
            heapq.heappop(rank)

        answer.append(rank[0])
    return answer
'''