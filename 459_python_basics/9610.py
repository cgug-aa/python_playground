#사분면 [브론즈 3]

def solution(N):
    count=[0, 0, 0, 0, 0]
    for i in range(N):
        a, b=map(int, input().split())
        if a==0 or b==0:
            count[4]+=1
        elif a>0 and b>0:
            count[0]+=1
        elif a>0 and b<0:
            count[3]+=1
        elif a<0 and b>0:
            count[1]+=1
        else:
            count[2]+=1
    print(f'Q1: {count[0]}')
    print(f'Q2: {count[1]}')
    print(f'Q3: {count[2]}')
    print(f'Q4: {count[3]}')
    print(f'AXIS: {count[4]}')

n=int(input())
solution(n)