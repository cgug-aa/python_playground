# 2007년 [브론즈 1]
import sys
input=sys.stdin.readline

X, Y = map(int, input().split())

m_31=[1, 3, 5, 7, 8, 10, 10]
m_30=[4, 6, 9, 11]
days=0
for m in range(1, X):
    if m in m_31:
        days+=31
    elif m in m_30:
        days+=30
    else:
        days+=28
days+=Y

w=days%7

if w==0:
    print('SUN')
elif w==1:
    print('MON')
elif w==2:
    print('TUE')
elif w==3:
    print('WED')
elif w==4:
    print('THU')
elif w==5:
    print('FRI')
elif w==6:
    print('SAT')