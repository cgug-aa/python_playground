# 사전 만들기

from collections import defaultdict

N=int(input())
dictionary=defaultdict(list)

for _ in range(N):
    s=input()
    dictionary[len(s)].append(s)
for n in sorted(list(dictionary.keys())):
    strings=sorted(list(set(dictionary[n])))
    for s in strings:
        print(s)