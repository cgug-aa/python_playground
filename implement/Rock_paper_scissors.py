# 가위 바위 보 프로그래머스 [레벨 1]

rps1='2'
rps2='205'

def solution(rps):
    answer=''
    for char in rps:
        if char=='0':
            answer+='5'
        elif char=='2':
            answer+='0'
        else:
            answer+='2'
    return answer

print(solution(rps1))
print(solution(rps2))

'''
더 나은 solution: 딕셔너리와 리스트 컴프리헨션을 사용해 간단하게 풀 수 있다.
def solution(s):
    win={'0':'5', '2':'0', '5':'2'}
    return ''.join([win[char] for char in s])
'''