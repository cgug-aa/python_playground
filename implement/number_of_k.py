# k의 개수 프로그래머스 [레벨 0]
import sys
input=sys.stdin.readline

def solution(i, j, k):
    count=0
    for n in range(i, j+1):
        while 1:
            n, rem=divmod(n, 10)
            if rem==k:
                count+=1
            if n==0:
                break
    return count

i, j, k=map(int, input().split())
print(solution(i, j, k))

'''
내 풀이: divmod를 사용하여 몫과 나머지를 구분하고, 나머지를 통해 모든 자리수를 순회한다.

solution:
def solution(i, j, k):
    return sum(str(num).count(str(k)) for num in range(i, j+1))

컴프리헨션은 신이야..
'''