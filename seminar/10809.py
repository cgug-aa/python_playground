# 알파벳 찾기

import sys
input=sys.stdin.readline

string=input().rstrip()
index=[-1 for _ in range(26)]

for idx, c in enumerate(string):
    if index[ord(c)-97]== -1:
        index[ord(c)-97] = idx
answer=''
for i in index:
    answer+=str(i)+' '
print(answer)
