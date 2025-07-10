# 압축된 수열

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
file = input().rstrip()

tmp=['0','1','2','3','4','5','6','7','8','9']
i=10
tmp_file=file

while 1:
    if i>62:
        print('-1')
        break
    if len(tmp_file)<=M:
        print(i)
        break
    tmp_file=''
    i+=1
    if i<37:
        tmp.append(chr(i+54))
    else:
        tmp.append(chr(i+60))
    frag=list(map(int, file.split()))
    
    for f in frag:
        q = 1
        tran=''
        while q > 0:
            q, r = divmod(f, i)
            f=f//i
            tran+=tmp[r]

        tmp_file+=tran[::-1]+' '
    tmp_file=tmp_file.rstrip()