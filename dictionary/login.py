# 로그인 성공? 프로그래머스 [레벨 0]

id_pw=["meosseugi", "1234"]
db=[["rardss", "123"], ["meosseugi", "1234"],["yyoom",'1234']]

def solution(id_pw, db):
    answer="fail"
    for d in db:
        if id_pw[0]==d[0]:
            answer='wrong pw'
            if  id_pw[1]==d[1]:
                answer='login'
    return answer

print(solution(id_pw, db))

"""
내 코드는 db의 데이터를 리스트로 사용하기 때문에 속도가 느리다.

풀이) 리스트를 딕셔너리로 바꿔서 코드를 실행한다.(딕셔너리로 변환은 리스트나 셋은 가능하다.)
def solution(id_pw, db):
    res=dict(db).get(id_pw[0])
    if res:
        if res==id_pw[1]:
            return "login"
        return "wrong pw"
    return "fail"
- 키의 값 = get(키)
"""