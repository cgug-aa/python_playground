#누울 자리를 찾아라 [실버 5]

N=int(input())
space=[]
count_row=0
count_col=0
for i in range(N):
    mat=list(input())
    space.append(mat)
    mat=[]
for i in range(N):
    seat=0
    for j in range(N):
        if space[i][j]=='X'or j==(N-1):
            if space[i][j]=='.':
                seat+=1
            if seat>=2:
                count_row+=1
            seat=0 
        else:
            seat+=1

for i in range(N):
    seat=0
    for j in range(N):
        if space[j][i]=='X'or j==(N-1):
            if space[j][i]=='.':
                seat+=1
            if seat>=2:
                count_col+=1
            seat=0   
        else:
            seat+=1
print(count_row, count_col)

#왜 오답일까요.. 다시 풉시다.
'''
N=int(input())
space=[]
count_row=0
count_col=0
for i in  range(N):
    mat=list(input())
    space.append(mat)
    mat=[]
for i in range(N):
    for j in range(N-1):
        if space[i][j]==space[i][j+1] and space[i][j]=='.':
            count_row+=1
            break
    for j in range(N-1):
        if space[j][i]==space[j+1][i] and space[j][i]=='.':
            count_col+=1
            break
print(count_row, count_col)
'''
#-> 한 줄에 2개 이상의 자리가 있는 경우를 고려하지 않음