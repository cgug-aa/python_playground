# 전자레인지 [브론즈 3]

def solution(T):
    if T%10 != 0:
        print(-1)
    else:
        a=T//300
        T%=300
        b=T//60
        T%=60
        c=T//10
        print(a, b, c)

T=int(input())
solution(T)