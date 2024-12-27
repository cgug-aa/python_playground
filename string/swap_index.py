#인덱스 바꾸기(일반적인 문자열) 프로그래머스 [레벨 0]

my_string1='hello'
t1_num1, t1_num2 = 1, 2

my_string2='I love you'
t2_num1, t2_num2 = 3, 6

def solution(my_string, num1, num2):
    tmp1, tmp2 = my_string[num2], my_string[num1]
    answer=''
    for n in range(len(my_string)):
        if n==num1:
            answer+=tmp1
        elif n==num2:
            answer+=tmp2
        else:
            answer+=my_string[n]
    print(answer)

solution(my_string1, t1_num1, t1_num2)
solution(my_string2, t2_num1, t2_num2)


'''

내 풀이 근거:
my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
이렇게 작성하면 바뀔 줄 알았지만, 불가능함.
-> 새로 문자열을 만들어서 return

sol) 내 풀이의 문제점을 해결하기 위해
def solution(my_string, num1, num2):
    string=list(my_string)
    string[num1], string[num2] = string[num2], string[num1]
    return "".join(string)

-> ','.join(['a', 'b', 'c', 'd'])   #a,b,c,d
-> ''.join(['a', 'b', 'c', 'd'])    #abcd
cf) join은 문자열이나 리스트의 원소가 문자인 리스트에 적용 가능하다.
cf) my_string[num1], my_string[num2] = my_string[num2], my_string[num1]은 리스트에서 가능하다.
cf) list를 str로 바꾸면 '[' ']', ',' 과 같은 문자도 포함된다. 
cf) 문자열을 슬라이싱해서 풀이할 수 있다.

'''