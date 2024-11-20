# 큰수의 법칙 [2019 국가 교육기관 코딩 테스트/난이도: 1]

import sys
import time
input=sys.stdin.readline

N, M, K=list(map(int, input().split()))
num=list(map(int, input().split()))
num.sort()

#첫번째 솔루션: M만큼 조건문+계산
s=time.time()
sum=0
count=0
for _ in range(M):
    count+=1
    if count==K:
        count=0
        sum+=num[-2]
    else:
        sum+=num[-1]
e=time.time()
print(f'{sum}, {e-s:.8f}')
'''
#두번째 솔루션: K로 나눈 나머지를 활용한다.
s=time.time()
sum2=0
while M>0:
    t=M%K
    sum2+=num[-1]*t

    M-=t
    if M>0:
        M-=1
        sum2+=num[-2]
e=time.time()
print(f'{sum2}, {e-s:.20f}')
'''
# 솔루션:
s=time.time()
count=int(M/(K+1))*K
count+=M%(K+1)

result =0
result+=count*num[-1]
result+=(M-count)*num[-2]
e=time.time()
print(f'{result}, {e-s:.20f}')