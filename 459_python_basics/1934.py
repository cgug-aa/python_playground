#최소공배수 [브론즈 1]

#최대공약수
#   주어진 두 수 중 더 작은 값부터 시작하여 숫자를 1씩 줄여가며, 나머지가 0인 수를 출력한다.
#   for i in range(min(A, B), 0, -1):
#       if i % A==0 and B%i==0:
#           print(i)
#           break
#최소공배수
#   (주어진 두 수 중 더 큰 값)을 시작으로 (주어진 두 수의 곱+1)까지 숫자를 1씩 늘려가며, 나머지가 0인 수를 출력
#   for i in range(max(A, B), (A*B)+1):
#       if i%a == 0 and i%b == 0:
#           print(i)
#           break 

#내 솔루션 -> 시간 초과
# 문제 해결방안 2가지
# 1. math 라이브러리에 gcd, lcm 함수를 사용
# 2. 유클리드 호제법
import math
N=int(input())
num=[]
for _ in range(N):
    a, b = map(int, input().split())
    num.append(math.lcm(a, b))
print(*num)