# 계단

m, j = map(int, input().split())
count=0

while m<j:
    count+=1
    m+=3

while m!=j:
    count+=1
    m-=1
print(count)