# 기차와 파리

X, Y, Z = map(int, input().split())

#기차의 속도
V = 2*Y

# 기차 속도: 파리 속도 = 기차 이동거리 : 파리 이동거리
move = Z * X // V
print(move)