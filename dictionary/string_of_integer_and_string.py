# 숫자 문자열과 영단어(2021 카카오 채용연계형 인턴십) 프로그래머스 [레벨 1]
from collections import defaultdict

s1='one4seveneight'
nums=defaultdict(int)
letter=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for idx, s in enumerate(letter):
    nums[s]=str(idx)

def solution(s):
    tmp=''
    answer=''
    for l in s:
        tmp+=l
        if tmp.isdigit():
            answer+=tmp
            tmp=''
        elif tmp in nums.keys():
            answer+=nums[tmp]
            tmp=''
    return int(answer)

print(solution(s1))

'''
솔루션)
def solution(s):
    for key, value in nums.items():
        s=s.replace(key, value)
    return int(s)

!!딕셔너리에 매몰되어 문자열을 잊지 말자!!

---
키-값의 딕셔너리를 만들 때, 값으로 키를 검색해야 하는 경우가 생긴다면

sol1) [key for key, value in aa.items() if value == 'value']
를 작성할 수 있지만, 딕셔너리 전체를 순회해야하므로 비효율적이다.

이럴 땐, sol2) {키-값}을 {값-키}로 저장하는 것이 좋다.
'''