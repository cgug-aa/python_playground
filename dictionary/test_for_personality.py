# 성격 유형 검사하기 프로그래머스 [레벨 1]
from collections import defaultdict

survey1=["AN", "CF", "MJ", "RT", "NA"]
choices1=[5, 3, 2, 7, 5]
survey2=["TR", "RT", "TR"]
choices2=[7, 1, 3]
scores=defaultdict(int)
for i in range(7):
    scores[i+1]=i-3
# scores={
#     1:-3,
#     2:-2,
#     3:-1,
#     4: 0,
#     5: 1,
#     6: 2,
#     7: 3
# }

def solution(survey, choices):
    count=defaultdict(int)
    for s, c in zip(survey, choices):
        if s.count("R")==1:
            count['1번 문항']+=scores[c] if s[0]=='R' else -(scores[c])
        elif s.count("C")==1:
            count['2번 문항']+=scores[c] if s[0]=='C' else -(scores[c])
        elif s.count("J")==1:
            count['3번 문항']+=scores[c] if s[0]=='J' else -(scores[c])
        elif s.count("A")==1:
            count['4번 문항']+=scores[c] if s[0]=='A' else -(scores[c])
    
    answer=""
    answer+="R" if count['1번 문항']<=0 else "T"
    answer+="C" if count['2번 문항']<=0 else "F"
    answer+="J" if count['3번 문항']<=0 else "M"
    answer+="A" if count['4번 문항']<=0 else "N"

    return answer

print(solution(survey1, choices1))
print(solution(survey2, choices2))

"""
defaultdict를 적극 활용하여 scores와 count를 선언한다.
"""