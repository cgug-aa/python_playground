# 문자열 계산하기 프로그래머스 [레벨 0]

my_string='3 + 5 - 5 + 12'
#print(eval(my_string))

'''
주의: eval은 절대로 사용해서는 안된다.
- 매우 위험하고 보안상 취약한 방법
- eval을 쓰지 않고 해결할 수 있는 방법이 거의 항상 존재
'''
result=0
m=1
my_list=my_string.split()
for c in my_list:
    if c.isdigit():
        tmp=int(c)
        if m==1:
            result+=tmp
        else:
            result-=tmp
    elif c=='-':
        m=-1
    else:
        m=1
print(result)

'''
int('-1')는 -1이 된다.

sol)
answer=0
for num in my_string.replace('-', '+ -').split('+'):
    answer+=int(num)
print(answer)

'''