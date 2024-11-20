# 숫자 야구 게임 [2019 국가 교육기관 코딩 테스트 난이도: 1]

import sys
input=sys.stdin.readline

N, M=list(map(int, input().split()))
result=min(list(map(int, input().split())))
for _ in range(N-1):
    m=min(list(map(int, input().split())))
    
    #이거 좀 짜쳐
    result=m if m>result else result

    #이렇게 바꿔서 쓰자
    result=max(m, result)

print(result)