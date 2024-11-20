# 1이 될 때까지 [2018 E 기업 알고리즘 대회]

import sys
input=sys.stdin.readline
N, K=list(map(int, input().split()))
count=0

while N>1:
    N=N/K if N%K==0 else N-1
    count+=1

print(count)