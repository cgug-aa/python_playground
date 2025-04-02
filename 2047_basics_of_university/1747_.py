#소수&팰린드롬 [실버 1]
#시간 초과 다시 풀기

N=int(input())
while 1:
    count=0
    N+=1
    for i in range(1, N+1):
        if N%i==0:
            count+=1
    if count==2:
        reversed_N=int(str(N)[::-1])
        if N==reversed_N:
            print(N)
            break
        else:
            pass
    else:
        pass

#정수 뒤집기, 문자열 뒤집기
#   1)정수 뒤집기
#       i) 슬라이싱 사용: [시작:끝:조건]
#
""" 다시 풀었는데 또 못 품,,
import sys
input=sys.stdin.readline
N=int(input().rstrip())
i=3
g=False
prime_num=[2]
while 1:
    print(prime_num)
    if i < N:
        for p in prime_num:
            if i%p==0:
                break
            else:
                g=True
        if g:
            g=False
            prime_num.append(i)

    elif i>=N:
        for p in prime_num:
            if i%p==0:
                break
            else:
                g=True
        if g:
            g=False
            if str(i)==str(i)[::-1]:
                print(i)
                break         
    i+=1
"""