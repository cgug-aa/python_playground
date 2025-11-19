# 시험 감독 [브론즈 2]

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
A = list(map(lambda x:x-B, A))

cnt=N

for a in A:
    if a>0:
        p, q = divmod(a, C)
        cnt+= p if q==0 else p+1
    
print(cnt)