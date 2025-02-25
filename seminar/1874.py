# 스택 수열
import sys
from collections import deque
input=sys.stdin.readline
N=int(input().rstrip())
seq=deque([int(input().rstrip()) for _ in range(N)])
stack=[]
cal=[]


for i in range(1,N+1):
    stack.append(i)
    cal.append('+')
    while seq[0]==stack[-1]:
        stack.pop()
        seq.popleft()
        cal.append('-')
        if len(seq)==0 or len(stack)==0:
            break

if len(stack)>0:
    print("NO")
else:
    for c in cal:
        print(c)
