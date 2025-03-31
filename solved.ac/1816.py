# 암호 키 [브론즈 1]
# import math
import sys
input=sys.stdin.readline
output=sys.stdout.write

N=int(input().rstrip())
for _ in range(N):
    num = int(input())
    flag = 1
    for i in range(2, 10**6+1):
        if num % i == 0:
            flag = 0
            break
    print("YES") if flag else print("NO")

"""
브루트포스 알고리즘: 그냥 피지컬로 누르기
"""


# for _ in range(N):
#     S=int(input().rstrip())
#     prime=[True for _ in range(2, S)]
#     for i in range(2, int(math.sqrt(S)) + 1):
#         if prime[i] == True:
#                     j = 2
#         while i * j <= S -2:
#             prime[i * j] = False
#             j += 1

#     prime = [idx+2 for idx, value in enumerate(prime) if value]
#     check=1
#     for p in prime:
#         if S%p==0:
#             check=0
#             break
#     if check:
#         output("YES\n")
#     else:
#         output("NO\n")
