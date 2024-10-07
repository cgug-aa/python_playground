#트리의 부모 찾기 [실버 2]

# 아이디어: 딕셔너리로 트리를 저장.
# 노드의 부모를 키로 갖고, 자식을 value로 갖는다.

N=int(input())
tree={1:[]}
node=[]
for _ in range(N-1):
    node.append(list(map(int, input().split())))

# 노드 리스트에서 딕셔너리의 키로 존재하는 원소를 포함하는 리스트 원소가 있으면 뽑아서 트리와 잇는다.
for n in node:
    if n[0] or n[1] in tree.keys():
    if n1 in tree.keys():
        tree[n1].append(n2)
        tree[n2]=[]
    elif n2 in tree.keys():
        tree[n2].append(n1)
        tree[n1]=[]
    else:
            # 이 경우도 고려해서 코드 작성해야 돼
            pass
for i in range(2, N+1):
    for key, value in tree.items():
        if i in value:
            print(key)
            break
