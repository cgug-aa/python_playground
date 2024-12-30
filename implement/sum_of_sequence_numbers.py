# 연속된 수의 합 프로그래머스 [레벨 0]

import sys
input=sys.stdin.readline

def solution(num, total):
    mid=total/num
    start=int(mid-num//2+0.5)
    result=[start+i for i in range(num)]
    return result

for _ in range(4):
    a, b= map(int, input().split())
    print(solution(a, b))

'''
내 풀이의 핵심 아이디어: 반올림을 할 때 +0.5 후 int()로 자료형을 바꿔준다.
'''