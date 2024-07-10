#더하기 사이클 [브론즈 1]

count=0
N=int(input())
new=N
while 1:
    new_10=int(new/10)
    new_1=new%10
    tmp=(new_1+new_10)%10
    new=new_1*10+tmp
    count+=1
    if new==N:
        print(count)
        break