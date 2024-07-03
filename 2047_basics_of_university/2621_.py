#카드 게임 [실버 2]

# 좀더 내공을 쌓고 다시 도전.

card=[]

R_count=0
B_count=0
Y_count=0
G_count=0

#주어진 카드 5장
for i in range(5):
    card.append(list(input().split()))
    if card[i][0]=='R':
        R_count+=1
    elif card[i][0]=='B':
        B_count+=1
    elif card[i][0]=='Y':
        Y_count+=1
    else:
        G_count+=1

#첫번째 규칙
if max(R_count, B_count, Y_count, G_count)==5:
    num=[]
    for i in range(5):
        num.append(int(card[i][1]))
    num.sort()
    i=0
    while num[i+1]-num[i]==1:
        i+=1
        if i==4:
            print(num[-1]+900)
            break

#두번째 규칙
elif max(R_count, B_count, Y_count, G_count)<=2:
    num=[]
    for i in range(9):
        num.append(4)
    for i in range(5):
        sub=int(card[i][1])
        num[sub-1]-=1
    if min(num)==0:
        print(num.index(0)+1+800)
    elif min(num)==1:
        a=num.index(1)
        num.remove(1)
        if min(num)==2:
            print(num.index(2))
            print((a+1)*10+num.index(2)+1+700)