#최소공배수 [브론즈 1]

T=int(input())
for j in range(T):
    A, B=map(int, input().split())
    for i in range(max(A, B), (A*B)+1):
        if i%A == 0 and i%B == 0:
            print(i)
            break 

#최대공약수
#   주어진 두 수 중 더 작은 값부터 시작하여 숫자를 1씩 줄여가며, 나머지가 0인 수를 출력한다.
#   for i in range(min(A, B), 0, -1):
#       if i % A==0 and B%i==0:
#           print(i)
#           break
#최대공배수
#   (주어진 두 수 중 더 큰 값)을 시작으로 (주어진 두 수의 곱+1)까지 숫자를 1씩 늘려가며, 나머지가 0인 수를 출력
#   for i in range(max(A, B), (A*B)+1):
#       if i%a == 0 and i%b == 0:
#           print(i)
#           break 