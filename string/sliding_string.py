# 문자열 밀기(일반적인 문자열) 프로그래머스 [레벨 0]

example1_A='hello'
example1_B='ohell'
example2_A='apple'
example2_B='elppa'
example3_A='atat'
example3_B='tata'
example4_A='abc'
example4_B='abc'

def solution(A, B):
    AA=A+A
    answer=0
    for i in range(len(A), -1, -1):
        if AA[i:i+len(A)]==B:
            return answer
        else:
            answer+=1
    return -1

print(solution(example1_A, example1_B))
print(solution(example2_A, example2_B))
print(solution(example3_A, example3_B))
print(solution(example4_A, example4_B))

'''
내 풀이
: A 문자열을 2배 하여 크기가 len(A)인 윈도우를 슬라이딩하여 B와 같은 부분을 찾는다.
'''