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