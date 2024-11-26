# 게임을 만든 동준이 [실버 4]

# 아이디어
# 뒤에서부터 계산하며, 마지막 숫자를 최대로 선정하고,
# 만나는 숫자를 현재 숫자보다 1만 작게 만든다.

import sys
input=sys.stdin.readline

N=int(input().rstrip())
nums=[]
for _ in range(N):
    nums.append(int(input().rstrip()))

nums.reverse()
result=0
for i in range(1, len(nums)):
    if nums[i-1]<=nums[i]:
        result+=nums[i]-nums[i-1]+1
        nums[i]=nums[i-1]-1
print(result)