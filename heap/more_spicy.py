# 더 맵게 프로그래머스 [레벨 2]
scoville1=[1, 2, 3, 9, 10, 12]
k1=7

def solution(scoville, k):
    count=0
    scoville.sort()
    while scoville[0]<k and len(scoville)>=2:
        a=scoville.pop(0)
        b=scoville.pop(0)
        scoville.insert(0, a+(b*2))
        scoville.sort()
        count+=1
    if min(scoville)>=k:
        print(count)
    else: print(-1)

solution(scoville1, k1)

'''
풀이) 최소힙을 사용하는 방법
def solution(scoville, k):
    num_foods=len(scoville)
    heapq.heapify(scoville)
    score=heapq.heappop(socville)

    idx=0
    while idx<num_foods-1 score <k:
        heapq.heappush(scoville, score + heapq.heappop(scoville)*2)
        score=heapq.heappop(scoville)
        idx+=1

    return -1 if score <k else idx
'''