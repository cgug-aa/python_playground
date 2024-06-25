#소수&팰린드롬 [실버 1]

N=int(input())
a=[]
i=N
while 1:
    for j in range(1, i+1):
        if i%j==0:
            a.append(j)
    if len(a)==2:
        str_i=str(i)
        list_i=list(str_i)
        reverse_list_i=reversed(list_i)
        if str_i==reverse_list_i:
            print(i)
            break
    else:
        a=[]
        i+=1
