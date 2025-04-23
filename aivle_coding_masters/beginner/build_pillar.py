# 기둥 세우기

N, M = map(int, input().split())
field=[list(map(int, input().split())) for _ in range(N)]

rows_idx = [idx for idx, f in enumerate(field) if 0 not in f]
cols_idx = []

for idx in range(M):
    t=True
    for i in range(N):
        if field[i][idx]==0:
            t=False
            break
    if t:
        cols_idx.append(idx)
print(max(len(rows_idx), len(cols_idx)))