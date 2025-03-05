# 최대 힙 [실버 2]
import heapq
import sys
input=sys.stdin.readline

N=int(input().rstrip())
hq=[]
heapq.heapify(hq)
for _ in range(N):
    i=int(input().rstrip())
    i=-i
    if i==0:
        if len(hq)==0:
            print(0)
        else:
            print(-(heapq.heappop(hq)))
    else:
        heapq.heappush(hq,i)