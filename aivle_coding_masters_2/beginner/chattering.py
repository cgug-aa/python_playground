# 채터링

N, K = map(int, input().split())
string = input()
answer=''
for s in string:
    answer+=(s*K)
print(answer)