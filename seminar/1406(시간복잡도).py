# 에디터 [실버 2]
import sys

input=sys.stdin.readline

string=input().rstrip()
M=int(input().rstrip())
cursor=len(string)

for _ in range(M):
    cmd=list(input().split())
    if cmd[0]=='L':
        cursor-=1 if cursor>0 else 0
    elif cmd[0]=='D':
        cursor+=1 if cursor<len(string) else 0
    elif cmd[0]=='B':
        if cursor==0:
            continue
        string=string[:cursor-1]+string[cursor:]
        cursor-=1

        
    elif cmd[0]=='P':
        string=string[:cursor]+str(cmd[1])+string[cursor:]
        cursor+=1
    else:
        break

print(string)

'''
- 파이썬에서 문자열은 immutable(변경 불가능)한 자료형이므로
    , 문자열을 수정할 때마다 새로운 문자열 객체를 생성해야한다.
    -> 문자열을 deque로 활용하여 시간 복잡도를 줄인다.

'''
