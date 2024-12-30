#치킨 쿠폰 프로그래머스 [레벨 0]

import sys
input=sys.stdin.readline

def solution(num):
    count=0
    while 1:
        coupon=num//10
        num//=10
        num+=coupon
        count+=coupon
        if num<10:
            return int(count)
for _ in range(2):
    a = int(input())
    print(solution(a))

'''
오답) 내 풀이는 치킨을 시키고 받은 쿠폰만 고려했다.
    -> 쿠폰으로 주문하고 받은 쿠폰도 고려해야 한다.

def solution(chicken):
    count=0
    while True:
        coupon=chicken//10
        chicken-=9*coupon
        count+=coupon
        if not coupon:
            break
    return count

'''