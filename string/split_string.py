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

