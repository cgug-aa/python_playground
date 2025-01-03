# 잘라서 배열로 저장하기 프로그래머스 [레벨 0]

my_str_1='abc1Addfggg4556b'
n1=6
my_str_2='abcdef123'
n2=3

def solution(my_str, n):
    arr=[]
    i=0
    while True:
        if len(my_str)>i+n:
            arr.append(my_str[i:i+n])
        else:
            arr.append(my_str[i:])
            return arr
        i+=n

print(solution(my_str_1, n1))
print(solution(my_str_2, n2))


'''
solution by comprehension
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, lem(my_str), n)]
시작 인덱스를 0부터 n만큼 증가시키고,
인덱스가 len(my_str)을 넘지 않도록 range 함수를 사용한 것이 차이점
'''