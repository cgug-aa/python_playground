#ATM [실버 4]

#가장 처리 시간이 짧은 사람부터 처리해야 총 소요시간이 가장 짧음

N=int(input())
time=list(map(int, input().split()))

time.sort()
count=0
for idx in range(N):
    count+=time[idx]*(N-idx)

print(count)