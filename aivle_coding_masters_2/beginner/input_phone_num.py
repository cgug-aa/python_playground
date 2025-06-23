#전화번호 입력

S = input()
if S.count('-')!=2:
    print('invalid')
else:
    numbers = list(S.split('-'))
    if numbers[0]=='010' and len(numbers[1])==4 and len(numbers[2])==4:
        print('valid')
    else:
        print('invalid')