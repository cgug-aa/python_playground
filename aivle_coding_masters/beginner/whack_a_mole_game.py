# 두더지 게임

import sys
input=sys.stdin.readline

count=0
# 행과 열의 합이 홀수일 때 두더지가 못나옴
for idx in range(8):
    row=input().rstrip()
    for i, s in enumerate(row):
        if s=="F" and (idx+i)%2==0:
            count+=1

print(count)