# 정렬된 많은 원소 사이에서 특정 원소 찾기

N, tgt = input().split()
nums=input().replace(' ','')
r=nums.find(tgt)
if r!=-1:
    print(int(r)+1)
else:
    print(r)