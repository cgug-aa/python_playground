# 계단 오르기 [실버 3]
# 다이나믹 프로그래밍!
# 아이디어: 1 1 2/ 2 1 1

import sys
input=sys.stdin.readline

N=int(input().rstrip())
stair=[]
for _ in range(N):
    stair.append(int(input().rstrip()))

print(stair)



# 다이나믹 프로그래밍(DP)이란..
# 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법
# 
# - DP의 목적:
#      메모리를 사용해서(=배열 혹은 자료구조를 만든다) 중복 연산을 줄이고(=연산한 값을 배열에 담는다.),
#      중복 연산을 줄여서 수행 속도를 개선한다.
#
# - 어떤 상황에 DP를 적용할지
#       1. BFS/DFS로 풀 수 있지만, 너무 경우의 수가 많을 때
#       2. 경우의 수들에 중복 연산이 많은 경우
#
#  - DP식 사고방식 적용하기(30분 정도 풀어보고 안되면 다양한 풀이 찾아보기)
# 참고: https://youtu.be/0bqfTzpWySY?si=JQFIymLqGlV9YGSq