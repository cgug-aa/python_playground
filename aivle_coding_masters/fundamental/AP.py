# 등차수열

import sys
input=sys.stdin.readline
output=sys.stdout.write
A, B, N=map(int, input().split())
output(str(A+B*(N-1)))