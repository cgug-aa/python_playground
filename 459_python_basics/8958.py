#OX 퀴즈 [브론즈 2]

T=int(input())
for i in  range(T):
    sum=0
    score=0
    string=input()
    for j in range(len(string)):
        if string[j]=='O':
            score+=1
            sum+=score
        else:
            score=0
    print(sum)