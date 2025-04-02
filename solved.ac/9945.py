# Centriod of Point Masses [브론즈 3]

import sys
input=sys.stdin.readline

case_num=1
while True:

    N=int(input().rstrip())
    
    if N<0:
        break
    Mx=0
    My=0
    M=0
    for _ in range(N):
        x, y, m = map(int, input().split())
        Mx+=x*m
        My+=y*m
        M+=m
    print('Case {}: {:.2f} {:.2f}'.format(case_num, Mx/M, My/M))
    case_num+=1
    input().rstrip()