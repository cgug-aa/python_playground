# 두라무리 휴지
from collections import defaultdict
import sys
input=sys.stdin.readline


N=int(input().rstrip())
s1=input().rstrip()
s2=input().rstrip()

def f1(string1, string2):
    d1=defaultdict(int)
    d2=defaultdict(int)
    
    for c in string1:
        d1[c]+=1
    for c in string2:
        d2[c]+=1

    return True if d1==d2 else False

def f2(string1, string2):
    return True if string1[0]==string2[0] and string1[-1]==string2[-1] else False

def f3(string1, string2):
    remove_char=['a', 'e', 'i', 'o', 'u']
    for c in remove_char:
        string1=string1.replace(c, '')
        string2=string2.replace(c, '')
    return True if string1==string2 else False

if f1(s1, s2) and f2(s1, s2) and f3(s1, s2):
    print('YES')
else:
    print('NO')