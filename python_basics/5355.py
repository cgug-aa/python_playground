#화성 수학
#다시 풀기



T=int(input())
string=[]
for i in range(T):
    string[i].append(input())
    string[i].replace(' ', '')
#for i in range(T):
#    result=string[i][0]


'''
1) replace&eval
string=[]
for i in range(T):
    string.append(input())
    string[i]=string[i].replace('@', '* 3')
    string[i]=string[i].replace('%', '+ 5')
    string[i]=string[i].replace('#', '- 7')    

for i in range(T):
    print(eval(string[i]))
'''

'''
2)문자열 슬라이싱 시도
test=[]
j=1
for i in range(T):
    string=input()
    test.append(string)
for i in range(T):
    result=float(test[i][0])
    for j in range(len(test[i])):
        if test[i][j]=='@':
            result*=3
        elif test[i][j]=='%':
            result+=5
        elif test[i][j]=='#':
            result-=7
        j+=1
    print(result)
'''


#idea1= 문자열 슬라이싱 -> 숫자가 합쳐지지 않는 problem
#idea2= replace & 연산자의 우선순위가 포함되어 원하는 것과 다르게 나옴.
#idea3= 조건문으로 계산
# 
#  문자열.replace('바꿀 문자', '바뀔 문자') !이건 원본 문자열에 저장되지 않으므로, 새로운 변수로 받아줘야 돼
#
