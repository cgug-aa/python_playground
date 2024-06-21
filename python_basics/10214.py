#baseball


T=int(input())
for i in range(T):
    Yonsei=[]
    Korea=[]
    for j in range(9):
        Y, K=map(int, input().split())
        Yonsei.append(Y)
        Korea.append(K)
    if sum(Yonsei)>sum(Korea):
        print('Yonsei')
    elif sum(Yonsei)<sum(Korea):
        print('Korea')
    else:
        print('Draw')
    