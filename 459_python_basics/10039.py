# 평균 점수 [브론즈 4]

import sys
input=sys.stdin.readline

score=[]
for _ in range(5):
    num=int(input().rstrip())
    score.append(num if num>=40 else 40)

print(sum(score)//5)