#트리의 부모 찾기 [실버 2]

# 아이디어: 노드의 부모를 저장하는 배열을 만든다.

import sys

input=sys.stdin.readline

N=int(input().rstrip())
node=[0 for _ in range(N)]
queue=[]

def list_insert(n1, n2):
    if n1==1:
        node[n2-1]=1
    elif n2==1:
        node[n1-1]=1
    else:
        if node[n1-1]!=0:
            node[n2-1]=n1
        elif node[n2-1]!=0:
            node[n1-1]=n2
        else:
            queue.append([n1, n2])
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    list_insert(n1, n2)

while node.count(0)!=1:
    for q in queue:
        if node[q[0]-1]==0:
            node[q[0]-1]=q[1]
            queue.remove(q)
        elif node[q[1]-1]==0:
            node[q[1]-1]=q[0]
            queue.remove(q)

for i in range(1, N):
    print(node[i])