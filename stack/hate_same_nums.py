# 같은 숫자는 싫어 프로그래머스 [레벨 1]

arr1=[1, 1, 3, 3, 0 , 1, 1]
arr2=[4, 4, 4, 3, 3]

def solution(arr):
    answer=[arr[0]]
    for num in arr:
        if num==answer[-1]:
            continue
        else:
            answer.append(num)
    return answer

print(solution(arr1))
print(solution(arr2))