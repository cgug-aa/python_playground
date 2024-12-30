# 369 게임 프로그래머스 [레벨 0]

def solution(order):
    result=0

    num=list(str(order))
    result+=num.count('3')
    result+=num.count('6')
    result+=num.count('9')

    return result

print(solution(29423))

'''
풀이
def solution(order):
    count=0
    for num in str(order):
        if num in ['3', '6', '9']
            count+=1
    return count

    문자열을 for문으로 돌리면 한 문자씩 출력된다.
    문자열에 여러 문자를 검색할 땐 리스트를 사용할 수 있다.
'''