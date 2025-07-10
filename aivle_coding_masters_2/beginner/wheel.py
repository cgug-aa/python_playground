# 톱니바퀴
import sys
from math import gcd, lcm

input = sys.stdin.readline
A, B, C = map(int, input().split())

#A에 대한 C의 배율
ratio = A/C

i=1
while i*ratio<10:
    i+=1
print(i)