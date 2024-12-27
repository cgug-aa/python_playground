# 자릿수 더하기(일반적인 문자열) 프로그래머스 [레벨 0]

input1=1234
input2=930211

def solution(num):
    answer=0
    for _ in range(len(str(num))):
        answer+=num%10
        num//=10
    return answer

print(solution(input1))
print(solution(input2))

'''
cf) divmod 내장함수 사용해보기
    몫, 나머지 = divmod(나누어지는 숫자, 나눌 숫자)
    2, 1 = divmod(5,2)

    while num:
        quo, rem = divmod(num, 10)
        answer+=rem
        num=quo

'''