# ZOAC 4 [브론즈 3]

#아이디어: 앉을 수 있는 열의 개수(홀수 열) * 앉을 수 있는 행(홀수 행)의 개수
H, W, N, M=map(int, input().split())
r=0
c=0

for i in range(1, H+1):
    if i%(1+N)==1:
        r+=1
for i in range(1, W+1):
    if i%(1+M)==1:
        c+=1

print(r*c)