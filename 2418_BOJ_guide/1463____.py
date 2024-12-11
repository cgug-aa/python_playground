# 1로 만들기 [실버 3]

# 아이디어:
# 우선 순위를 두어 1, 2, 3 method 순으로 그리디한다.

import sys
input=sys.stdin.readline

N=int(input().rstrip())
count=0
while N!=1:
    count+=1
    if N%3==0:
        N/=3
    elif N%2==0:
        N/=2
    else:
        N-=1
    print(N, count)
print(count)

# 다이나믹 프로그래밍