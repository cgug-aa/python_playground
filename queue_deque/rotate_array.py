# 배열 회전시키기 프로그래머스 [레벨 0]
from collections import deque

numbers1=deque([1, 2, 3])
direction1="right"
numbers2=deque([4, 455, 6, 4, -1, 45, 6])
direction2="left"

def solution(number, direction):
    if direction=='left':
        number.rotate(-1)
    else:
        number.rotate()
    print(number)

solution(numbers1, direction1)
solution(numbers2, direction2)