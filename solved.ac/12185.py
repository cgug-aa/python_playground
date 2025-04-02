# GBus count(Large) [브론즈 2]

import sys
input=sys.stdin.readline

T=int(input().rstrip())
for t in range(T):
    N=int(input().rstrip())
    A_to_B=list(map(int, input().split()))
    C=int(input().rstrip())
    
    possible=[]
    for _ in range(C):
        c=int(input().rstrip())
        count=0
        for idx in range(N):
            if A_to_B[2*idx]<=c and c <= A_to_B[2*idx+1]:
               count+=1
        possible.append(count)

    print(f"Case #{t+1}:", end='')
    for p in range(len(possible)):
        print(f" {p}", end='')