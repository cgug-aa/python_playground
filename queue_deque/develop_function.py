# 기능 개발 프로그래머스 [레벨 2] '''틀림'''
from collections import deque
progresses1=deque([93, 30, 55])
speeds1=deque([1, 30, 5])
progresses2=deque([95, 90, 99, 99, 80, 99])
speeds2=deque([1, 1, 1, 1, 1, 1])

def solution(progresses, speeds):
    successes=deque()
    top=1
    count=0
    while 0<=len(progresses):
        for i, s in enumerate(speeds):
            progresses[i]+=s
            if (progresses[i]>=100) and (progresses[i]-s<100):
                successes.append(i+1)
        if successes:
            while successes[-1]==top:
                top+=1
                successes.pop()
                count+=1
                if not successes:
                    print(count, end=' ')
                    count=0
                    break
        print(progresses,successes)
        count+=1

#solution(progresses1, speeds1)
#solution(progresses2, speeds2)

'''
내 풀이의 문제점: 성공한 데크를 만들고, 한번의 비교를 추가하려고 했음.

풀이: 앞에서부터 100의 값이 넘으면 넘는개수 만큼 count를 올리고, progress와 speeeds를 하나씩 빼준다.
def solution2(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []

    while progresses:
        # 하루 동안 작업 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0
        # 맨 앞 작업이 완료되었으면 배포
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        
        if count:
            answer.append(count)

    print(answer)  # [1, 3, 2]

solution2(progresses2, speeds2)
'''