# N과 M (1)

from itertools import permutations

N, M = map(int, input().split())
pools=[i for i in range(1, N+1)]

for p in permutations(pools, M):
    print(str(p).replace(',', '').replace('(','').replace(')',''))