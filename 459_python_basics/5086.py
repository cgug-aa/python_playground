# 배수와 약수 [브론즈 3]

import sys
input=sys.stdin.readline

while 1:
    a, b=list(map(int, input().split()))
    if a==0 and b==0:
        break
    if b%a==0:
        print('factor')
    elif a%b==0:
        print('multiple')
    else:
        print('neither')