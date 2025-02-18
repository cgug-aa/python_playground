# 콜라츠 추측 프로그래머스 [레벨 1]

n1=6
n2=16
n3=626331
count=0
limit=500

def solution(num):
    global count
    if num==1:
        return count
    
    if count<limit:
        count+=1
    else:
        return -1
    
    if num%2==0:
        return solution(num/2)
    elif num%2==1:
        return solution(num*3+1)
    
print(solution(n1))
print(solution(n2))
print(solution(n3))

"""
전역 변수의 값을 변경(재할당)하면 global을 선언해야 한다. = count
전역 변수를 읽기만 하면 global 선언이 필요 없다.         = limit
"""