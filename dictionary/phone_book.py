# 전화번호 목록 프로그래머스 [레벨 2]


phone_book1=['119', '97674223', '1195524421']
phone_book2=['123', '456', '789']
phone_book3=['12', '123', '1235', '567', '88']

def solution(phone_book):
    for idx, p in enumerate(phone_book):
        for i in range(idx, len(phone_book)):
            if idx != i and p==(phone_book[i])[:len(p)]:
                return False
    return True

print(solution(phone_book1))
print(solution(phone_book2))
print(solution(phone_book3))

'''
내 풀이) 선택한 요소를 제외한 값을 비교하며 순회

solution) 
- 전화부를 정렬하고, 직후 문자와만 비교하기 (정렬하였기 때문에 이웃한 전호부만 비교하면 된다.)
- 문자열 비교할 때, startswith(문자열)로 비교하였다.

def solution(phone_book):
    phone_book=sorted(phone)
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
'''