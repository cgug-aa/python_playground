# 림보게임

N=int(input())
hgt=list(map(int, input().split()))
check=True
for h in hgt:
    if h>160:
        continue
    check=False
    print('I', h)
    break
if check:
    print('P')