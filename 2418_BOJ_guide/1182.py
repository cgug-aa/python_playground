# 부분수열의 합 [실버 2]
from itertools import combinations

N, S=map(int, input().split())
seq=list(map(int, input().split()))
result=0
for i in range(1, N+1):
    for p in combinations(seq, i):
        if sum(p)==S:
            result+=1
print(result)