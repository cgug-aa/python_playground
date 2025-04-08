# 아까운 쿠폰

N=int(input())
answer=0
for d in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
    q, r = divmod(N, d)
    answer+=q
    N-=d*q
    if not N:
        break
print(answer)