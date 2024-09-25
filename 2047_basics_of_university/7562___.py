# 나이트의 이동 [실버 1]

T=int(input())

for _ in range(T):
    L=int(input())
    
    start=list(map(int, input().split()))
    end=list(map(int, input().split()))


# 나이트의 시작 위치를 통해 체스판에 갈 수 있는 위치는 정해진다.
# 아이디어:
# 시작 위치와 도착 위치의 행의 차와 열의 차를 확인
# 나이트가 이동하면서 행:2 열:1을 이동하든 행:1 열:2를 이동하든 둘 중 하나이다.
