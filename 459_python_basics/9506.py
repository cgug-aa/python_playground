#약수들의 합 [브론즈 1]

while 1:
    num=[1]
    n=int(input())
    if n==-1:
        break
    else:
        for i in range(n-1,1,-1):
            if n%i==0:
                num.append(i)
        num.sort()
        if sum(num)==n:
            print(f'{n} = {num[0]}', end='')
            for i in range(1, len(num)):
                print(f' + {num[i]}', end='')
            print('')
        else:
            print(f'{n} is NOT perfect.')