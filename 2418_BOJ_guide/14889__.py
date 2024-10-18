#스타트와 링크 [실버 1]

# 문제를 푸는 방법 2가지
# 1) 조합 2) 백트래킹

# 케이스의 개수가 생각보다 많지 않음 => 조합으로 풀어보자
# 번호 조합에 따른 팀 전력을 set에 담고 min값을 출력

import sys
from itertools import combinations as c
from itertools import permutations as p

input=sys.stdin.readline
N=int(input().rstrip())

mat=[]
for _ in range(N):
    row = list(map(int, input().split()))
    mat.append(row)

case=list(c(range(N), N//2))
result=set()
for ca in case:
    team_s=list(p(ca, 2))
    team_l=list(p(set(range(N))-set(ca), 2))
    sum_s=0
    sum_l=0
    for t in team_s:
        i, j=t[0], t[1]
        sum_s+=mat[i][j]
    for t in team_l:
        i, j=t[0], t[1]
        sum_l+=mat[i][j]
    result.add(abs(sum_s-sum_l))

print(min(result))

# 가져가야할 개념: 백트래킹
# 알고리즘 기법 중 하나로 재귀적으로 문제를 해결하되,
# 현재 재귀를 통해 확인 중인 상태가 제한 조건에 위배가 되는지 판단하고,
# 해당 상태가 위배되는 경우 해당 상태를 제외하고 다음 단계로 넘어간다.
# KEY POINT = 더 이상 탐색할 필요가 없는 상태를 제외한다는 것인데, 이를 가지치기라고 한다.