# 프로세스 프로그래머스 [레벨 2]
from collections import deque

priorites1=deque([2, 1, 3, 2])
location1=2
priorites2=deque([1, 1, 9, 1, 1, 1])
location2=0

def solution(priorites, location):
    count=0
    while len(priorites)>=0:
        if priorites[0]==max(priorites):
            count+=1
            if location==0:
                print(count)
                break
            priorites.popleft()
            location-=1

        else:
            priorites.rotate(-1)
            location-=1
        
        if location==-1:
            location=len(priorites)-1

solution(priorites1, location1)
solution(priorites2, location2)