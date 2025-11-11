# 덩치 [실버 5]

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    bigger = 0
    for j in range(n):
        if i==j: pass
        pa, pb = people[i]
        na, nb = people[j]
        if pa<na and pb<nb:
            bigger+=1
    print(bigger+1, end=' ')