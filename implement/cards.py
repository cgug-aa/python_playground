# 카드 뭉치 프로그래머스 [레벨 1]

import sys
input=sys.stdin.readline

def solution(card_list1, card_list2, goals):
    i, j = 0, 0
    for g in goals:
        if i==len(card_list1) or j==len(card_list2):
            return 'No'
        
        if card_list1[i]==g:
            i+=1
        elif card_list2[j]==g:
            j+=1
        else:
            return 'No'
    return 'Yes'
        
card1=list(input().split())
card2=list(input().split())
goal=list(input().split())
print(solution(card1, card2, goal))

'''
내 풀이 아이디어: 인덱스 두 개를 사용하여 각각 리스트를 순회한다.
'''