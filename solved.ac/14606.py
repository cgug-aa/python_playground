# 피자 (Small) [실버 5]

import sys
input=sys.stdin.readline
output=sys.stdout.write
N=int(input().rstrip())
answer=0
while N>1:
    N-=1
    answer+=N
output(str(answer))