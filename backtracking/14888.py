# 연산자 끼워넣기 [실버 1]
# 백트래킹 문제인데, 파이썬 라이브러리로 풀었음. -> 이게 맞는지 모르겠네

import sys
from  itertools import permutations
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
mth = []
mthd = ['+','-', '*', '//']
for i, v in enumerate(list(input().split())):
    if v!='0':
        cnt = int(v)
        while(cnt>0):
            mth.append(mthd[i])
            cnt-=1

chk = True
for c in set(permutations(mth, N-1)):   
    rs =seq[0]

    for m ,s in zip(c, seq[1:]):
        if m=='+': rs+=s
        elif m=='-': rs-=s
        elif m=='*': rs*=s
        else: 
            if rs < 0:
                rs *= (-1)
                rs //= s
                rs *= (-1)
            else:
                rs//=s

    if chk:
        max_val = rs
        min_val = rs
        chk = False
        continue

    max_val = max(max_val, rs)
    min_val = min(min_val, rs)

print(max_val)
print(min_val)