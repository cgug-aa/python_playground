#수 찾기 [실버 4]

import sys
input=sys.stdin.readline

N=int(input().rstrip())
N_list=set(map(int, input().split()))

M=int(input().rstrip())
M_list=list(map(int, input().split()))

for m in M_list:
    print(1) if m in N_list else print(0)

# problem) 리스트로 비교하면 시간이 너무 오래 걸림
# solution) list가 아닌 set으로 풀어보자
# 리스트에서의 x in X 연산 시간 복잡도: O(n)
# 세트에서의 x in X 연산 시간 복잡도: O(1)
# 세트 시간복잡도가 1인 이유
# => 세트는 해시 테이블로 구현되어 있기 때문이다.
# 해시테이블: 입력값이 들어오면 해시 함수를 통해 key-value 형식으로 저장하기 때문이다.