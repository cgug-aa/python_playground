# Anti Multiply Array

from itertools import combinations

N = int(input())
arr = list(map(int, input().split()))

found = False

# 네 개의 서로 다른 인덱스를 고른다
for a, b, c, d in combinations(arr, 4):
    # 두 쌍을 나누는 방법은 3가지:
    # (a*b == c*d), (a*c == b*d), (a*d == b*c)
    if a * b == c * d or a * c == b * d or a * d == b * c:
        found = True
        break

print("YES" if found else "NO")