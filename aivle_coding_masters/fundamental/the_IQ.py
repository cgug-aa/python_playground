# 우리반 아이큐왕은?

import sys
input=sys.stdin.readline

N=int(input().rstrip())
stu=[]
for _ in range(N):
    a, b = input().split()
    stu.append([a, int(b)])
stu.sort(key=lambda x: x[1], reverse=True)

print(stu[0][0])
print(stu[1][0])
print(stu[2][0])