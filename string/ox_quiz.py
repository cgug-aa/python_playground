# OX 퀴즈 프로그래머스 [레벨 0]
import sys
input=sys.stdin.readline

n=int(input().rstrip())
quiz=[input().rstrip() for _ in range(n)]

for q in quiz:
    left, right=q.split(' = ')
    result=0
    for num in left.replace('-', '+-').replace(' ', '').split('+'):
        result += int(num)

    print('O') if result==int(right) else print('X')
    
print(quiz)

'''
strip()는 문자열 양쪽의 공백을 없애기만 하고, 문자열 사이에 있는 공백은 지우지 못한다.
문자열 중간에 있는 문자을 지우고 싶다면, replace를 사용하는 것이 좋다.
left.replace('-', '+ -').strip().split('+')
> 3 + - 4
> 3, - 4 로 나눠지게 됨.
'''