# 주식 [실버 2]
# 아이디어:
# 1. 감소하지 않는 구간을 찾는다.
# 2. 증가하는 동안에는 매일 사고, 증가의 마지막날에 판다.

# 아이디어의 문제점:
# 앞에서부터 계산하면서 불필요한 계산이 포함된다.
# 주식의 최고 가격인 지점을 메모리에 저장하고 사용하기 위해 뒤에서부터 계산한다.
# 이를통해 다른 리스트를 사용하지 않고 계산이 가능하다.

import sys
input=sys.stdin.readline

T=int(input().rstrip())

for _ in range(T):
    N=int(input().rstrip())
    nums=list(map(int, input().split()))
    result=0
    '''
    cal=[]
    for i in range(N):
        if i==0 or nums[i]>=cal[-1] :
            cal.append(nums[i])
        else:
            for c in cal:
                result+=max(cal)-c
            cal=[nums[i]]
        if i==N-1:
            for c in cal:
                result+=max(cal)-c
    '''
    max_price = 0  # 현재까지의 최대 가격

    # 뒤에서부터 탐색
    for price in reversed(nums):
        if price > max_price:
            max_price = price  # 새로운 최대 가격 갱신
        else:
            result += max_price - price  # 이익 계산

    print(result)

# 그리디의 경우 역으로 계산하는 경우로 풀리는 경우가 다수 존재,
# reverse 계산 고려하기