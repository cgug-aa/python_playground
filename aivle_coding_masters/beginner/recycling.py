# 분리수거장

import math
N=int(input())
apt_peo=[list(map(int,input().split())) for _ in range(N)]


min_distance=math.inf
answer=0

for idx, apt in enumerate(apt_peo):
    tmp=0
    for t1, t2 in apt_peo:
        tmp+=abs(t1-apt[0])*t2
    
    if min_distance>tmp:
        min_distance=tmp
        answer=idx
print(answer+1)