# 요세푸스 문제 <실버5>

import sys
from collections import deque

input=sys.stdin.readline

N, K=map(int, input().split())
deq=deque(range(1, N+1))
output=[]
while len(deq)!=0:
    deq.rotate(-(K-1))
    output.append(deq.popleft())

output=str(output).replace('[', '<').replace(']', '>')
print(output)



'''
파이썬 라이브러리를 활용하자.

시간초과 원인: nums 리스트에서 K번째 요소를 계속해서 찾고 제거하는 방식이 비효율적이기 때문
-> 원형 큐를 활용한다.

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque(range(1, N + 1))
output = []

while queue:
    # K-1번 회전하여 K번째 요소가 첫 번째 위치에 오도록 함
    queue.rotate(-(K - 1))
    # 첫 번째 위치의 요소를 제거하고 결과 리스트에 추가
    output.append(queue.popleft())

# 출력 형식 조정
print("<" + ", ".join(map(str, output)) + ">")

----------
시간 효율성을 고려하여 알고리즘 짜기
deque를 적극활용
- rotate에 대해 이해하기
    a.rotate(1)
    = 오른쪽으로 1만큼 밀기
    
    1, 2, 3, 4, 5
    -> 5, 1, 2, 3, 4 
'''