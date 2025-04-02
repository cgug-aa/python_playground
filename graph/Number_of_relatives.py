# 촌수 계산 [실버 2]
from collections import defaultdict
import sys
input=sys.stdin.readline

n=int(input().rstrip())
t1, t2=map(int, input().split())
t1_ascen=[]
t2_ascen=[]
layer=int(input().rstrip())
relation=defaultdict(list)

for _ in range(layer):
    p, d = map(int, input().split())
    relation[p].append(d)

def find_root(ascen, node):
    parent=0
    for p, d in relation.items():
        if node in d:
            parent=p
    if parent==0:
        return ascen
    else:
        ascen.append(parent)
        return find_root(ascen, parent)
    
find_root(t1_ascen, t1)
find_root(t2_ascen, t2)

if t1_ascen[-1]==t2_ascen[-1]:
    for _ in range(min(len(t1_ascen), len(t2_ascen))):
        if t1_ascen[-1]!=t2_ascen[-1]:
            break
        t1_ascen.pop()
        t2_ascen.pop()
        
    print(len(t1_ascen)+len(t2_ascen)+2)
else:
    print(-1)
