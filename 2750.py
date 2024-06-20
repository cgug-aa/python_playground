#수 정렬하기

N=int(input())
list=[]
for i in range(0, N):
    a=input()
    list.append(a)
#print(list)

for i in range(1, N):
    select=list[i-1]
    if list[i]<select:
        list[i], list[i-1] = list[i-1], list[i]

print(list)