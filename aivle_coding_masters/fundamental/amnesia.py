# 기억상실

A, B, N = map(int, input().split())
N-=B
m, n =divmod(N, A-B)
result = m+1 if n else m
print(result)