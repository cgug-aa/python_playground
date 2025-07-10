# 선물

N=int(input())
gift=sorted(list(map(int, input().split())))
answer = 1
i = 1

while i < gift[-1]:
    check=True
    for g in gift:
        if g%i != 0:
            check=False
            break
    if check:
        answer = i
    i+=1
print(answer)