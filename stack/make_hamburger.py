# 햄버거 만들기 프로그래머스 [레벨 1]

ingredient1=[2, 1, 1, 2, 3, 1, 2, 3, 1]
ingredient2=[1, 3, 2, 1, 2, 1, 3, 1, 2]

def solution(ingredient):
    stacks=[]
    i=0
    for i in ingredient:
        if i==1:
            if type(stacks[i])=='list':
                if stacks[i][-1]==3:
                    answer+=1
                    stacks.pop(-1)
                    i-=1
                else:
                    i+=1
                    stacks[i].append([1])
        elif i==2:
            if stacks[i][-1]==1:
                stacks[i][-1].append(2)


print(solution(ingredient1))
print(solution(ingredient2))

'''
출제의도 파악의 중요성
111122331111 난 이게 2인줄 알았음
             솔루션에선 0임.


'''