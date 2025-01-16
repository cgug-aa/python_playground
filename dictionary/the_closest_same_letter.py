# 가장 가까운 같은 글자 프로그래머스 [레벨 1]
from collections import defaultdict
s1="banana"
s2='foobar'
last_index1=defaultdict(int)
last_index2=defaultdict(int)
def solution(s, last_index):
    answer=[]
    for idx,l in enumerate(s):
        if last_index[l]==0:
            answer.append(-1)
            last_index[l]=idx+1
        else:
            answer.append(idx-last_index[l]+1)
            last_index[l]=idx+1
    return answer

print(solution(s1, last_index1))
print(solution(s2, last_index2))

"""
defaultdict로 딕셔너리 선언하고, 이를 카운팅해서 사용한다.
"""