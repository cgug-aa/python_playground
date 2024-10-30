# 약수 [브론즈 1]

#아이디어: 두번째 줄에 주어지는 숫자들은 어떤 수 N의 1과 N을 제외한 약수들이다
#         어떤 수 N을 구하려면 약수들을 정렬했을 때, 첫값과 두번째 값을 곱한값과 같다.
import sys
input=sys.stdin.readline
print=sys.stdout.writelines

num=int(input().rstrip())
numbers=list(map(int, input().rstrip().split()))
numbers.sort()
print(str(numbers[0]*numbers[-1]))