# 최빈값 구하기 프로그래머스 [레벨 0]
from collections import defaultdict

arr1=[1, 2, 3, 3, 3, 4]
arr2=[1, 1, 2, 2]
arr3=[1]
def solution(arr):
    nums_count=defaultdict(int)
    for num in arr:
        nums_count[num]+=1
    max=0
    for k in nums_count.keys():
        if nums_count[k]>=max:
            if max!=nums_count[k]:
                max=nums_count[k]
                answer=k
            else:
                answer=-1
    return answer

print(solution(arr2))
print(solution(arr2))
print(solution(arr3))

'''
내 풀이) key값을 카운팅하는 딕셔너리를 만들고, 순회하며 비교

sol)
def solution(array):
    while array:
        for idx, val in enumerate(set(array)):
            array.remove(val)
        if not idx:
            return val
    return -1
> array를 집합으로 만들고, array에서 집합의 원소를 하나씩 지운다.
  처음에는 idx가 0보다 큰 값이지만, 
  원소를 지우다 마지막 한 개만 남은 경우 인덱스가 0이 된다.
  이때 val를 리턴하면 이게 최빈값이 된다.
  만일 이 과정을 끝까지 반복했는데도 지워지지 않는 다른 값이 있다면 -1을 리턴하면 된다.

  *발상적이라 내가 코테에서 쓸 수는 없을듯..?*     
'''