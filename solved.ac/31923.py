# 마라탕후루 [브론즈 2]
import sys
input=sys.stdin.readline

N, P, Q = map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
answer=[]
for s1, s2 in zip(a, b):
    count=0
    if s1==s2:
        answer.append(count)
        continue
    else:
        if P>Q:
            while s1 < s2:
                s1+=P
                s2+=Q
                count+=1
                
                if count>10000:
                    break
                if s1==s2:
                    answer.append(count)
        else:
            while s1 > s2:
                s1+=P
                s2+=Q
                count+=1
                if count>10000:
                    break
                if s1==s2:
                    answer.append(count)
if len(answer)==N:
    print("YES")
    print(' '.join(map(str, answer)))
else:
    print("NO")