# 삼각형의 조건

a, b, c = map(int, input().split())
if (a+b+c)!=180 or a<=0 or b<=0 or c<=0:
    print('F')
else:
    print('P')