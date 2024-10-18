# 프린터 큐 [실버 3]

import sys
from collections import deque
input=sys.stdin.readline

T=int(input().rstrip())
for _ in range(T):
    N, M=map(int, input().split())
    q=deque(map(int, input().split()))
    q=deque((i, idx) for idx, i in enumerate(q))
    count=1
    while len(q)>0:
        if q[0][0]==max(q, key=lambda x:x[0])[0]:
            if q[0][1]==M:
                print(count)
                break
            else:
                count+=1
            q.popleft()
        else:
            q.append(q.popleft())
            

# 코드가 좀 짜친데.. 다른 방법은?
# 개선 사항
# 1) 큐를 리스트로 사용하지말고, from collections import deque를 쓰자
# 2) find와 q를 이중리스트로 하나의 객체에 담자
# 3) max값 비교는 key=@@ 파라미터를 통해 구하자
# 4) @@를 lamba를 통해 추출해서 쓰자.
# 5) q.append(q.pop(0))으로 간단하게 작성할 수 있다.