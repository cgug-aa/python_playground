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
    for j in range(N-1):
        if space[i][j]==space[i][j+1] and space[i][j]=='.':
            count_row+=1
            break
    for j in range(N-1):
        if space[j][i]==space[j+1][i] and space[j][i]=='.':
            count_col+=1
            break
print(count_row, count_col)