#주사위 게임 [브론즈 3]

C=100
S=100
n=int(input())
for i in range(n):
    A, B=map(int, input().split())
    if A>B:
        S-=A
    elif B>A:
        C-=B
    else:
        pass
print(C)
print(S)