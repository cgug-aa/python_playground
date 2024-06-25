#Yangjojang of The Year [브론즈 1]

T=int(input())
Max=0
drink=[]
for _ in range(T):
    N=int(input())
    for i in range(N):
        drink.append(list(input().split()))
        Max=max(Max, int(drink[i][1]))
    for i in range(N):
        if int(drink[i][1])==Max:
            print(drink[i][0])

# 리스트 원소 추가하는 방법
# 값을 비교하는 방법 + max()내장함수 사용
