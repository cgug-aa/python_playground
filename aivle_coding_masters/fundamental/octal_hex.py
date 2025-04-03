# 8진수와 16진수

import sys
input=sys.stdin.readline
output=sys.stdout.write

N=int(input())
output(oct(N)[2:]+' '+hex(N)[2:].upper())