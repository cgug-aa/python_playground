# 동전 [실버 4]

N, K = map(int, input().split())
kind_of_money=[]

for _ in range(N):
    kind_of_money.append(int(input()))

count=0
kind_of_money.sort(reverse=True)
for m in kind_of_money:
    if K>=m:
        count+=K//m
        K=K%m
    if K==0: break
print(count)


# **시간 초과**
#     while K>=kind_of_money[i]:
#       K-=kind_of_money[i]
#       count+=1

#    if K>m:
#        count+=K//m
#        K=K%m