# 스캐너 [브론즈 1]

import sys
input=sys.stdin.readline

R, C, ZR, ZC = map(int, input().split())
def mul(word):
    return word*ZC
Rows=[list(map(mul,input().rstrip())) for _ in range(R)]

for r in range(R*ZR):
    print(str(Rows[r//ZR]).replace("'", "").replace(", ", "").replace("[", "").replace("]", ""))