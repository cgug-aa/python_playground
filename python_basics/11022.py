#A+B-8

T=int(input())
list=[]
for i in range(0, T):
    A, B=map(int, input().split())
    C=A+B
    list.append([A, B, C])

for i in range(1, T+1):
    print("Case #%d: %d + %d = %d" % (i, list[i-1][0], list[i-1][1], list[i-1][2]))

#T개의 (A, B)쌍을 입력받아, 마지막에 출력하는 기능
#list로 입력받은 A, B, C을 리스트로 저장하고 출력한다.
#list에 원소를 넣을 땐, append로...
#여러 숫자를 출력할 땐, %(c1, c2, c3...)