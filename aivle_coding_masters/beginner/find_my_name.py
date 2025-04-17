#  내 이름이 적힌 번호 찾기

N, tgt = input().split()
names=list(input().split())
for idx, name in enumerate(names):
    if tgt==name:
        print(idx+1)
        break