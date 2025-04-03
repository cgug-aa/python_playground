# 비밀번호 찾기 [기초]

import sys
input=sys.stdin.readline

passwd=input().replace(' ', '')
for idx, p in enumerate(passwd):
    if p=='c':
        result=' '.join(passwd[:idx+1]) if len(passwd)!=idx+1 else passwd
        print(result)
