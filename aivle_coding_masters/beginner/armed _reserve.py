# 예비군 훈련

info = list(input().split())

if info[0]=='0': print(0)
#병사의 경우
elif info[3]=='Private':
    if int(info[0])>=1 and int(info[0])<=4:
        if info[2]=='Y' or info[1]=='ROKAF':
            print(28)
        else:
            print(32)
    else:
        print(20)
#간부의 경우
else: 
    print(28)