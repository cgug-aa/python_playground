# 유사 소수 분할

# 1) N 이하의 유사 소수를 찾고
# 2) 유사 소수 분할 가능한지 찾는다.
import math
from itertools import combinations

N = int(input())

def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

def is_pseudo_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            j = n // i
            if i!=j and is_prime(i) and is_prime(j):
                return True
    return False
    
def pseudo_list(N):
    pseudo_prime=[]
    for i in range(2, N):
        if is_pseudo_prime(i):
            pseudo_prime.append(i)
 
    return pseudo_prime

pseudo_primes = pseudo_list(N)
# def solution(pseudo_primes):
#     check_list = list(combinations(pseudo_primes, 3))
#     for con in check_list:
#         a, b, c = con
#         if sum(con)<=N and (N-sum(con))!=a and (N-sum(con))!=b and (N-sum(con))!=c:
#             return True
#     return False

def solution(N, pseudo_primes):
    for a in range(1, N-2):
        for b in range(a+1, N-a-1):
            for c in range(b+1, N-a-b):
                d = N - a - b - c
                if d > c and len({a, b, c, d}) == 4:
                    cnt = sum(1 for x in [a, b, c, d] if x in pseudo_primes)
                    if cnt >= 3:
                        return True
    return False


if solution(N, pseudo_primes):
    print('possible')
else:
    print('impossible')