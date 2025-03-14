# 숫자 POP
import sys
input=sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
set_nums=set(nums)
set_nums=list(set_nums)

max_len=0
for s in set_nums:
    index_s=[]
    for idx, n in enumerate(nums):
        if n==s:
            index_s.append(idx)
    
    for i in index_s:
        count=K
        tmp=0
        for j in range(i, len(nums)):
            if s != nums[j]:
                if count==0:
                    break
                count-=1
            else:
                tmp+=1
        max_len = max(tmp, max_len)
print(max_len)