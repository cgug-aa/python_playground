# 외계어 사전 프로그래머스 [레벨 0]

spell1=['p', 'o', 's']
dict1=['sod', 'eocd', 'qixm', 'adio', 'soo']
spell2=['z', 'd', 'x']
dict2=['def', 'dww', 'dzx', 'loveaw']
spell3=['s', 'o', 'm', 'd']
dict3=['moos', 'dzx', 'smm', 'sunmmo', 'som']


def solution(spell, dict):
    spell_set=set(spell)
    for d in dict:
        d_set=set(d)
        if len(d_set | spell_set)==len(d_set):
            return 1
    return 2

print(solution(spell1, dict1))
print(solution(spell2, dict2))
print(solution(spell3, dict3))

'''
내 풀이의 단점: set의 경우 순서가 없기에 등호로 비교하면 되는데, 그렇게 하지않아 계산이 많아짐.

sol)
def solution(spell, dict):
    spell_set=set(spell)
    for d in dict:
        if set(d)==spell_set:
            return 1
    return 2
'''