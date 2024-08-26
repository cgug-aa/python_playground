# 보물 [실버 4]

def solution(N, a, b):
    a.sort()
    answer=0
    c=[0 for _ in range(N)]
    for i in range(N):
        Max=max(b)
        idx=b.index(Max)
        answer+=(Max*a[i])
        b[idx]=0
        c[idx]=a[i]

    print(answer)

N=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
solution(N, a, b)