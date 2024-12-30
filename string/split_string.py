# 문자열 나누기(일반적인 문자열) 프로그래머스 [레벨 1]

ex1='banana'
ex2='abracadabra'
ex3='aaabbaccccabba'

def solution(string):
    a, b = 0, 0
    answer=[]
    tmp=''
    for s in string:
        if a==0 and b==0: x = s
        if x==s: a+=1 
        else: b+=1
        if a==b:
            answer.append(tmp+s)
            a, b = 0, 0
            tmp=''
        else:
            tmp+=s
    if tmp:
        answer.append(tmp)
    print(answer)
    print(len(answer))

solution(ex1)
solution(ex2)
solution(ex3)

'''
내 풀이의 개선 요소:
- 불필요한 변수 선언(tmp, answer)

solution: 문자을 쪼갠다는 접근보다 point를 이동시킨다는 접근 필요
        -> 변수를 초기화한다 x 덮어쓴다 o 

def solution(s):
    count=0
    me=0
    other=0
    for char in s:
        if me==other:
            count+=1
            pre=char
        
        if char==pre:
            me+=1
        else:
            other+=1
    return count
'''