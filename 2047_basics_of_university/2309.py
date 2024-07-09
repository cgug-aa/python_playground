#일곱 난쟁이 [브론즈 1]

friends=[]
sum=0
for i in range(9):
    height=int(input())
    friends.append(height)
    sum+=height
hight_over=sum-100

for i in range(len(friends)):
    for j in range(i+1, len(friends)):
        if (friends[i]+friends[j])==hight_over:
            a, b=friends[i], friends[j]
            break
friends.remove(a)
friends.remove(b)
friends.sort()
for n in range(len(friends)):
    print(friends[n])