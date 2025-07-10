# Cup Covering [브론즈 2]

import sys
import math 
input=sys.stdin.readline


area=int(input().rstrip())
r = math.sqrt(area/(math.pi))
print(round(2*r, 10))