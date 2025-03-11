#Mini-Trtris 3023 [브론즈 2]

import sys
input=sys.stdin.readline

s, t, c = map(int, input().split())
result=s*2

if c>=2:
    c-=2
    result += t*2+3

result+=(c//2)*3

print(result)