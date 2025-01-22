# 중복된 문자 제거 프로그래머스 [레벨 0]

my_string1='people'
my_string2='We are the world'

def solution(my_string):
    answer=''
    my_string=set(my_string)
    for s in my_string:
        answer+=s
    return answer

print(solution(my_string1))
print(solution(my_string2))