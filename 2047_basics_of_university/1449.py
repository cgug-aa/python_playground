# 수리공 항승 [실버 3]

N, L = map(int, input().split())
leak_location=list(map(int, input().split()))
leak_location.sort()
count=0
for _ in range(N):
    length=[leak_location[0]+l for l in range(L)]
    for n in range(L):
        if length[n] in leak_location:
            leak_location.remove(length[n])
    count+=1
    if len(leak_location)==0:
        break
print(count)

#아이디어: 누수가 있는 곳 중 가장 앞 쪽부터 테이프를 붙인다.
# 이때 한번에 연결할 수 있는 누수 부분을 동시에 제거한다.