# 완주하지 못한 선수 프로그래머스 [레벨 1]

participant1=['leo', 'kiki', 'eden']
completion1=['eden', 'kiki']
participant2=['mislav', 'stanko', 'mislav', 'ana', 'mislav']
completion2=['stanko', 'mislav', 'ana']

def solution(participant, completion):
    for c in completion:
        participant.remove(c)
    return participant

print(solution(participant1, completion1))
print(solution(participant2, completion2))

'''
#풀이) Counter를 활용한다.
from collections import Counter
def solution2(participant, completion):
    participates=Counter(participant)
    completes=Counter(completion)
    return list((participates - completes))[0]
print(solution2(participant1, completion1))
print(solution2(participant2, completion2))

> 이러면 동명이인이 3명 이상일 경우에 문제가 발생할거같은디,,,

'''