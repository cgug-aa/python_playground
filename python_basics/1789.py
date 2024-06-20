#수들의 합
#다시풀기

S=int(input())
sum=0
N=0
i=0
while i<1:
    sum=(N+1)*(N)/2
    if sum>S:
        if (sum-S)>N:
            print(N+1)
        else:
            print(N)
        i+=1
    else:
        N+=1