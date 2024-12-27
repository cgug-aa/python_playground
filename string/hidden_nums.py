# 숨어 있는 숫자의 덧셈(문자열 메소드 사용) 프로그래머스 [레벨 0]

import sys
input=sys.stdin.readline

my_string=input().rstrip()

nums=[]
tmp=''
for s in my_string:
    if s.isdigit():
        tmp+=s
    else:
        if len(tmp)!=0:
            nums.append(int(tmp))
        tmp=''
print(sum(nums))

'''
풀이 핵심 아이디어: 문자열.isdigit()을 사용하여 숫자 문자를 판단

개선 사항: nums 리스트를 선언하지말고, 바로 결과값에 합하기 (메모리 절약)
nums=[]
answer=0
for s in my_string:
    if s.isdigit():
        tmp+=s
    else:
        if len(tmp)!=0:
            answer+=int(tmp)
        tmp=''
print(answer)
'''