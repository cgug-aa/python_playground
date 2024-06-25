#개표 [브론즈3]

V=int(input())
result=input()
'''
Sol1)문자열의 원소를 하나씩 비교해서 카운팅
A=0
B=0
for i in range(len(result)):

    if result[i]=='A':
        A+=1
    else:
        B+=1
if A>B:
    print('A')
elif A==B:
    print('Tie')
else:
    print('B')
'''

'''
Sol2)내장함수 count 활용해보기
# count(원하는 문자, 카운트하는 문자열의 시작 인덱스, 카운트하는 문자열의 마지막 인덱스)

if result.count('A')>result.count('B'):
    print('A')
elif result.count('A')==result.count('B'):
    print('Tie')
else:
    print('B')
'''