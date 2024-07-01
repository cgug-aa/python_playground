#문자열 반복 [브론즈 2]

T=int(input())
for i in range(T):
    N, string=input().split()
    N=int(N)
    for j in range(len(string)):
        print(string[j]*N, end='')
    print('')