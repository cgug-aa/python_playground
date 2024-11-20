#로프 [실버 4]
'''
내 풀이
import sys
input=sys.stdin.readline

n=int(input().rstrip())
weight=[]
for _ in range(n):
    weight.append(int(input().rstrip()))

weight.sort()
result=0

rop=[]
while True:
    rop.append(weight.pop())
    if result>min(rop)*len(rop):
        break
    result=min(rop)*len(rop)
    if len(weight)==0:
        break

print(result)'''

import sys
input = sys.stdin.readline

n = int(input().rstrip())
weight = [int(input().rstrip()) for _ in range(n)]

# 내림차순 정렬
weight.sort(reverse=True)

# 최댓값 계산
result = 0
for i in range(n):
    # 현재 로프를 포함해 병렬로 사용했을 때 들 수 있는 최대 무게
    max_weight = weight[i] * (i + 1)
    result = max(result, max_weight)

print(result)