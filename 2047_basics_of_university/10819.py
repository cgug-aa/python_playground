#차이를 최대로  [실버 2]

#|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]| 의 최대 값을 구하시오.
# 아이디어: 정렬하고 두 묶음으로 나눈 뒤
# 리스트의 홀수 인덱스에는 큰 수부터
# 리스트의 짝수 인덱스에는 작은 수부터 넣어 구한다.
# 
# -> N이 최대 8인데, 8!이 6700개 정도의 경우의 수면 다 계산하는게 나을 듯

import sys
from itertools import permutations
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
nums=list(map(int,input().rstrip().split()))
result=0
for l in list(permutations(nums)):
    s=0
    for n in range(N-1):
        s+=abs(l[n]-l[n+1])
    result=max(result, s)  
print(str(result))