#중복 빼고 정렬하기 [실버 5]

import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
numbers=list(set(map(int, input().rstrip().split())))
numbers.sort()
for n in numbers:
    print(str(n)+" ")