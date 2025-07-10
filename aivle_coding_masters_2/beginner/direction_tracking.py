# 방향 추적

import sys
input = sys.stdin.readline

N = int(input())
x, y = map(int, input().split())
for _ in range(N-1):
    v_x, v_y = map(int, input().split())
    if v_x - x == 0:
        if v_y-y>0:
            tmp=f'2 {abs(v_y-y)}'
        else:
            tmp=f'4 {abs(v_y-y)}'
    else:
        if v_x-x>0:
            tmp=f'1 {abs(v_x-x)}'
        else:
            tmp=f'3 {abs(v_x-x)}'
    print(tmp)
    x, y = v_x, v_y