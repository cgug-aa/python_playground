# 0= not cute / 1 = cute [브론즈 3]

N=int(input())
vote=[0, 0]
for _ in range(N):
    vote_idx=int(input())
    vote[vote_idx]+=1

print("Junhee is not cute!") if vote[0]>vote[1] else print("Junhee is cute!")