# 직각 삼각형

l = sorted(list(map(int, input().split())))
if l[2]**2==(l[0]**2)+(l[1]**2):
    print('YES')
else:
    print('NO')