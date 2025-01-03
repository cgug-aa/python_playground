# 가장 큰 수 찾기 프로그래머스 [레벨 0]

import sys
input=sys.stdin.readline

arr=list(map(int, input().split(',')))
def solution(arr):
    value=max(arr)
    idx=arr.index(value)
    return [value, idx]

print(solution(arr))

'''
내 풀이의 문제점: max를 사용하면, 최댓값을 찾는 데 시간 복잡도 O(n)이
                ,리스트에서 해당 값의 인덱스를 찾는 데 O(n)이 소요된다.

max와 index를 사용하지 않고 최댓값과 최댓값의 인덱스를 구하는 방법
def solution(arr):
    larget=0
    index=None
    for idx, num in eumerate(arr):
        if num > largest:
            largest = num
            index=idx
    return [largest, index]

cf) 정렬로도 풀 수 있다.
def solution(arr):
    val, index=list(sorted(enumerate(arr), key=lambda x: x[1])[-1])
    return index, val
'''