# 왕실의 나이트 [난이도 1]
# 8x8 체스판 위에 나이트의 위치를 입력하면 이동할 수 있는 위치 개수 리턴

dx=[1, 1, -1, -1, 2, 2, -2, -2]
dy=[2, -2, 2, -2, 1, -1, 1, -1]
point=input()

y, x = ord(point[0])-96, int(point[1])
count=0
for yp, xp in zip(dy, dx):
    fx=x+xp
    fy=y+yp
    if fx>0 and fx<9 and fy>0 and fy<9:
        count+=1
print(count)