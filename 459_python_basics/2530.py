#인공지능 시계 [브론즈 4]

time=list(map(int, input().split()))
T=int(input())
s=T%60
m=int(T/60)

time[1]+=m
time[2]+=s
while 1:
    if time[2]>=60:
        time[2]-=60
        time[1]+=1
    else: 
        break
while 1:
    if time[1]>=60:
        time[1]-=60
        time[0]+=1
    else: 
        break
while 1:
    if time[0]>=24:
        time[0]-=24
    else:
        break
print(*time)

#리스트의 요소를 출력하는 방법
#   1) for문 이용
#    for x in arr:
#    print(x, end = " ")
#   2) 애스터리스크(*) 사용
#    print(*arr)