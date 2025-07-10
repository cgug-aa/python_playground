# 마법의 지팡이

N = int(input())
count=0
while N%5==0:
    N = N//5 * 4
    count+=1
while N%3==0:
    N = N//3 *2
    count+=1
while N%2==0:
    N = N//2
    count+=1
if N!=1:
    print('-1')
else:
    print(count)