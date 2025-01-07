# 행렬의 덧셈 프로그래머스 [레벨 1]

t1_arr1=[[1, 2, 3],[2, 3, 4],[1, 2, 3]]
t1_arr2=[[3, 4, 5],[5, 6, 7],[1, 2, 3]]
t2_arr1=[[1],[2]]
t2_arr2=[[3],[4]]

def solution(arr1, arr2):
    answer=[]
    for ar1, ar2 in zip(arr1, arr2):
        row=[]
        for a1, a2 in zip(ar1, ar2):
            row.append(a1+a2)
        answer.append(row)
    return answer

print(solution(t1_arr1, t1_arr2))
print(solution(t2_arr1, t2_arr2))

'''
이 문제의 키는 정해지지 않은 행렬의 크기에 따른 처리일 듯

풀이)
조금 더 빠른 방법: 컴프리헨션을 활용한다.
def solution(arr1, arr2):
    answer=[[c+d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer
'''