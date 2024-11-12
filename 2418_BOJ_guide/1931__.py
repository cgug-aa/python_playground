#회의실 배정 [실버 1]

#아이디어:
# 회의가 끝나는 시간 순서대로 오름차순 정렬한다.

import sys
input=sys.stdin.readline

N=int(input().rstrip())
time_table=[]

for _ in range(N):
    meet=list(map(int, input().rstrip().split()))
    time_table.append(meet)

time_table.sort(key=lambda x:(x[1], x[0]))
count=0
prior=0
for t in time_table:
    if t[0]>=prior:
        prior=t[1]
        count+=1
print(count)