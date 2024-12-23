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
strip()으로 공백이 없어지지 않는 경우가 존재한다.
left.replace('-', '+ -').strip().split('+')
> 3 + - 4
> 3, - 4 로 나눠지게 됨.
'''