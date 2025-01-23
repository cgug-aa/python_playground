# 컨트롤 제트 프로그래머스 [레벨 0]

s1='1 2 Z 3'
s2='10 20 30 40'
s3='10 Z 20 Z 1'
s4='10 Z 20 Z'
s5='-1 -2 -3 Z'

def solution(s):
    nums=[]
    string=s.split()
    for n in string:
        if n=='Z':
            nums.pop(-1)
        else:
            nums.append(int(n))

    return sum(nums)

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))

'''
항상 자료형이 문자인지 숫자인지 생각하며 풀기
'''