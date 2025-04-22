# 몇 번씩 나올까

N=int(input())
nums_count={}

for n in range(10):
    nums_count[n]=0
for num in range(1, N+1):
    for n in list(str(num)):
        nums_count[int(n)]+=1

for p in nums_count.values():
    print(p, end=' ')