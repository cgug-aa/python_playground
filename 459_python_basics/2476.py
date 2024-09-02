# 주사위 게임 [브론즈 3]

# 주사위의 숫자를 담을 리스트
dice=[]
score=[]
# 주사위를 던지는 사람 수
N= int(input())

for _  in range(N):
    dice.append(list(map(int, input().split())))

for dice_case in dice:
    count=[0 for _ in range(6)]
    for num in dice_case:
        count[num-1]+=1
    Max=max(count)
    if Max==3:
        score.append(10000+1000*(count.index(3)+1))
    elif Max==2:
        score.append(1000+100*(count.index(2)+1))
    else:
        score.append(max(dice_case)*100)

print(max(score))